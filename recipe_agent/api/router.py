from fastapi import APIRouter
from recipe_agent.api.v1.endpoints import recipes
from recipe_agent.api.v1.endpoints import integrations

router = APIRouter()
router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
router.include_router(
    integrations.router, prefix="/integrations", tags=["integrations"]
)
