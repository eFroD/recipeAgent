from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from recipe_agent.db.database import get_db
from recipe_agent.db.models.users import User
from recipe_agent.db.models.api_keys import APIKey
from recipe_agent.core.security import oauth2_scheme, decode_token
from recipe_agent.auth.service import get_user_by_username

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

router = APIRouter()

# Schemas
class APIKeyCreate(BaseModel):
    service_name: str  # "mealie", "spotify", "notion", etc.
    api_key: str
    base_url: str | None = None

class APIKeyResponse(BaseModel):
    id: int
    service_name: str
    base_url: str | None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Get current user profile
@router.get("/me")
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user

# List all API keys for current user
@router.get("/me/api-keys", response_model=list[APIKeyResponse])
async def list_user_api_keys(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    keys = db.query(APIKey).filter(
        APIKey.user_id == current_user.id,
        APIKey.is_active
    ).all()
    return keys

# Add or update API key
@router.post("/me/api-keys", status_code=status.HTTP_201_CREATED)
async def create_or_update_api_key(
    api_key_data: APIKeyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    existing_key = db.query(APIKey).filter(
        APIKey.user_id == current_user.id,
        APIKey.service_name == api_key_data.service_name
    ).first()
    
    if existing_key:
        existing_key.api_key = api_key_data.api_key
        existing_key.base_url = api_key_data.base_url
        existing_key.is_active = True
        db.commit()
        return {"message": f"{api_key_data.service_name} API key updated successfully"}
    
    new_key = APIKey(
        user_id=current_user.id,
        service_name=api_key_data.service_name,
        api_key=api_key_data.api_key,
        base_url=api_key_data.base_url
    )
    db.add(new_key)
    db.commit()
    return {"message": f"{api_key_data.service_name} API key created successfully"}

# Get specific API key by service
@router.get("/me/api-keys/{service_name}", response_model=APIKeyResponse)
async def get_api_key_by_service(
    service_name: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    api_key = db.query(APIKey).filter(
        APIKey.user_id == current_user.id,
        APIKey.service_name == service_name,
        APIKey.is_active
    ).first()
    
    if not api_key:
        raise HTTPException(
            status_code=404, 
            detail=f"No active API key found for {service_name}"
        )
    
    return api_key

# Delete API key
@router.delete("/me/api-keys/{service_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_api_key(
    service_name: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    api_key = db.query(APIKey).filter(
        APIKey.user_id == current_user.id,
        APIKey.service_name == service_name
    ).first()
    
    if not api_key:
        raise HTTPException(
            status_code=404, 
            detail=f"API key for {service_name} not found"
        )
    
    db.delete(api_key)
    db.commit()
