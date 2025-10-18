from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from recipe_agent.api.v1.endpoints import recipes
from recipe_agent.api.v1.endpoints import integrations
from recipe_agent.core.database import get_db
from recipe_agent.core.security import oauth2_scheme, decode_token
from recipe_agent.auth.service import get_user_by_username
from recipe_agent.api.v1.endpoints import auth


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    username = payload.get("sub")
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


router = APIRouter(prefix="/api/v1")
router.include_router(auth.router, prefix="/auth", tags=["authentication"])
router.include_router(
    recipes.router,
    prefix="/recipes",
    tags=["recipes"],
    dependencies=[Depends(get_current_user)],
)
router.include_router(
    integrations.router,
    prefix="/integrations",
    tags=["integrations"],
    dependencies=[Depends(get_current_user)],
)
