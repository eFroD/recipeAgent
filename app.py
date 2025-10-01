from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from recipe_agent.agents.description_validator import recipe_validator
import logfire
import os

app = FastAPI()

logfire_token = os.environ.get("LOGFIRE_WRITE_TOKEN")
logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()
class VideoRequest(BaseModel):
    url: HttpUrl

@app.post("/extract-recipe")
async def extract_recipe(request: VideoRequest):
    try:
        response = await recipe_validator.run(f"Please extract the recipe from the given url: {request.url}")
        return {"recipe": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
