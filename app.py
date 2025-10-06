from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from recipe_agent.agents.video_agent import recipe_validator
from recipe_agent.models.output_models.recipe import Recipe
import logfire
import os

app = FastAPI()

logfire_token = os.environ.get("LOGFIRE_WRITE_TOKEN")
logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()


class VideoRequest(BaseModel):
    url: HttpUrl
    target_language: str = "english"


@app.post("/extract-recipe")
async def extract_recipe(request: VideoRequest):
    try:
        response = await recipe_validator.run(
            f"Please extract the recipe from the given url: {request.url}. The target language is {request.target_language}."
        )
        response.output.recipe = Recipe.model_validate(
            response.output.recipe
        ).model_dump_json(by_alias=True)
        response.output.suggested_version = Recipe.model_validate(
            response.output.suggested_version
        ).model_dump_json(by_alias=True)
        return {"recipe": response}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
