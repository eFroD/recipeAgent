from fastapi import APIRouter, HTTPException
from recipe_agent.models.input_models.video import VideoRequest
from recipe_agent.models.output_models.recipe import RecipeResponse
from recipe_agent.core.recipe_service import extract_recipe_from_url

router = APIRouter()


@router.post("/extract-recipe")
async def extract_recipe(request: VideoRequest) -> RecipeResponse:
    try:
        recipe = await extract_recipe_from_url(request)
        return recipe
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
