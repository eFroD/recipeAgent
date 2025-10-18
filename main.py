from fastapi import FastAPI
import logfire
import os
from recipe_agent.core.database import Base, engine
from recipe_agent.api.router import router
from recipe_agent.auth.router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Agent API", version="1.0.0")

logfire_token = os.environ.get("LOGFIRE_WRITE_TOKEN")
logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()

app.include_router(auth_router)
app.include_router(router)
