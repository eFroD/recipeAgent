from fastapi import FastAPI
import logfire
import os
from recipe_agent.api.router import router

app = FastAPI()

logfire_token = os.environ.get("LOGFIRE_WRITE_TOKEN")
logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()

app.include_router(router)
