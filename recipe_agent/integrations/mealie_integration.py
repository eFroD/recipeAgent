"""This module serves the functionality for communication with a Mealie instance."""

import os
import httpx
from pydantic import HttpUrl

MEALIE_ENDPOINT = os.environ.get("MEALIE_ENDPOINT", None).rstrip("/")
MEALIE_API_KEY = os.environ.get("MEALIE_API_KEY", None)

send_recipe_url = f"{MEALIE_ENDPOINT}/api/recipes"
check_user_url = f"{MEALIE_ENDPOINT}/api/users/self"


async def push_image_to_mealie(image_url: HttpUrl, slug: str) -> bool:
    """Uploads an image to a Mealie recipe asynchronously.

    Args:
        image_url: URL of the image to download and upload
        slug: The recipe slug identifier

    Returns:
        bool: True if successful
    """
    headers = {"Authorization": f"Bearer {MEALIE_API_KEY}"}

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Download the image asynchronously
        img_response = await client.get(str(image_url))
        img_response.raise_for_status()
        image_binary = img_response.content

        # Determine image extension from URL or content-type
        content_type = img_response.headers.get("content-type", "")
        if "jpeg" in content_type or "jpg" in content_type:
            extension = "jpg"
        elif "png" in content_type:
            extension = "png"
        elif "webp" in content_type:
            extension = "webp"
        elif "?" in str(image_url):
            # Handle URLs with query parameters
            extension = str(image_url).split("?")[0].split(".")[-1]
        else:
            # Fallback to extracting from URL
            extension = "jpg"

        # Prepare multipart form data
        files = {
            "image": ("image." + extension, image_binary, f"image/{extension}"),
            "extension": (None, extension),
        }

        # Upload to Mealie asynchronously
        response = await client.put(
            f"{MEALIE_ENDPOINT}/api/recipes/{slug}/image", headers=headers, files=files
        )
        response.raise_for_status()

    return True


async def push_recipe_to_mealie(recipe: dict) -> str:
    """Pushes a recipe to a Mealie instance asynchronously.

    Args:
        recipe: The recipe to be pushed.

    Returns:
        str: Success message
    """
    headers = {
        "Authorization": f"Bearer {MEALIE_API_KEY}",
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        print(recipe)
        response = await client.post(send_recipe_url, headers=headers, json=recipe)
        response.raise_for_status()
        slug = response.json()

    # Check if there is an image in the recipe and upload it separately
    if "image" in recipe and recipe["image"]:
        await push_image_to_mealie(recipe["image"], slug)

    return "Recipe pushed to Mealie successfully."


async def verify_mealie_user() -> bool:
    headers = {
        "Authorization": f"Bearer {MEALIE_API_KEY}",
        "accept": "application/json"
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(check_user_url, headers=headers)
        try:
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError:
            return False
