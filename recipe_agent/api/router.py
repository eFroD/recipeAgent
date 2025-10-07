from fastapi import APIRouter
from recipe_agent.api.v1.endpoints import recipes

router = APIRouter()
router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
