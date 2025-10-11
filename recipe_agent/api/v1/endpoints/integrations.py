from fastapi import APIRouter
from recipe_agent.models.output_models.recipe import Recipe
from recipe_agent.integrations.mealie_integration import push_recipe_to_mealie

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
