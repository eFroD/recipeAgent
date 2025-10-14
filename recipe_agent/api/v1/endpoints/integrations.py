from fastapi import APIRouter
from recipe_agent.models.output_models.recipe import Recipe
from recipe_agent.integrations.mealie_integration import push_recipe_to_mealie
from recipe_agent.integrations.mealie_integration import verify_mealie_user

router = APIRouter()


@router.post("/upload-mealie")
async def upload_to_mealie(recipe: Recipe):
    """
    Upload a recipe to Mealie.
    """
    response = await push_recipe_to_mealie(
        recipe.model_dump(by_alias=True, mode="json")
    )
    return response

@router.get("/verify-mealie-user")
async def verify_user_mealie():
    """
    Verify Mealie user credentials.
    """
    is_valid = await verify_mealie_user()
    return {"valid": is_valid}
