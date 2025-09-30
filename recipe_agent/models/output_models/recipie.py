from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl


class NutritionInformation(BaseModel):
    calories: Optional[str]
    fatContent: Optional[str]
    carbohydrateContent: Optional[str]
    proteinContent: Optional[str]
    fiberContent: Optional[str]
    sugarContent: Optional[str]
    servingSize: Optional[str]


class HowToStep(BaseModel):
    text: str
    image: Optional[HttpUrl]


class HowToSection(BaseModel):
    name: Optional[str]
    itemListElement: List[HowToStep]


class Ingredient(BaseModel):
    quantity: Optional[str]
    name: str


class Recipe(BaseModel):
    name: str
    description: Optional[str]
    image: Optional[Union[HttpUrl, List[HttpUrl]]]
    recipeYield: Optional[str]
    recipeIngredient: List[str]
    recipeInstructions: Optional[Union[List[HowToStep], List[HowToSection], str]]
    prepTime: Optional[str]            # Duration ISO 8601: e.g., "PT20M"
    cookTime: Optional[str]            # Duration ISO 8601
    totalTime: Optional[str]           # Duration ISO 8601
    recipeCategory: Optional[str]
    recipeCuisine: Optional[str]
    keywords: Optional[str]
    suitableForDiet: Optional[str]    # e.g., "GlutenFreeDiet"
    nutrition: Optional[NutritionInformation]
    author: Optional[str]
    aggregateRating: Optional[float]  # Simplified, could be complex object
    video: Optional[HttpUrl]          # Link to recipe video
