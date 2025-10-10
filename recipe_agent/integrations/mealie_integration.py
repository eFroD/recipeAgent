"""This module serves the functionality for communication with a Mealie instance."""
import os
import requests
from pydantic import HttpUrl
MEALIE_ENDPOINT = os.environ.get("MEALIE_ENDPOINT", None).rstrip("/")
MEALIE_API_KEY = os.environ.get("MEALIE_API_KEY", None)

login_url = f"{MEALIE_ENDPOINT}/api/auth/token"
send_recipe_url = f"{MEALIE_ENDPOINT}/api/recipes"


def push_image_to_mealie(image_url: HttpUrl, slug: str) -> str:
    """Uploads an image to a Mealie recipe.
    
    Args:
        image_url: URL of the image to download and upload
        slug: The recipe slug identifier
        
    Returns:
        str: Success message
    """
    headers = {"Authorization": f"Bearer {MEALIE_API_KEY}"}
    
    # Download the image
    img_response = requests.get(str(image_url))
    img_response.raise_for_status()
    image_binary = img_response.content
    
    # Determine image extension from URL or content-type
    content_type = img_response.headers.get('content-type', '')
    if 'jpeg' in content_type or 'jpg' in content_type:
        extension = 'jpg'
    elif 'png' in content_type:
        extension = 'png'
    elif 'webp' in content_type:
        extension = 'webp'
    else:
        # Fallback to extracting from URL
        extension = str(image_url).split('.')[-1].split('?')[0] or 'jpg'
    
    # Prepare multipart form data
    files = {
        'image': ('image.' + extension, image_binary, f'image/{extension}'),
        'extension': (None, extension)
    }
    
    # Upload to Mealie
    response = requests.put(
        f"{MEALIE_ENDPOINT}/api/recipes/{slug}/image",
        headers=headers,
        files=files
    )
    response.raise_for_status()
    
    return True


def push_recipe_to_mealie(recipe: dict) -> str:
    """Pushes a recipe to a Mealie instance.

    Args:
        recipe (Recipe): The recipe to be pushed.

    Returns:
        str: The response from the Mealie instance.
    """
    # Placeholder implementation
    #access_token = login_user()
    headers = {"Authorization": f"Bearer {MEALIE_API_KEY}",
                "accept": "application/json", 
                "Content-Type": "application/json"
                }
    response = requests.post(send_recipe_url, headers=headers, json=recipe)
    response.raise_for_status()
    slug = response.json()
    # Check if there is an image in the recipe and upload it separately
    if "image" in recipe and recipe["image"]:
        push_image_to_mealie(recipe["image"], slug)
    
    return "Recipe pushed to Mealie successfully."
