from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl, Field

class NutritionInformation(BaseModel):
    calories: Optional[str]
    fatContent: Optional[str]
    carbohydrateContent: Optional[str]
    proteinContent: Optional[str]
    fiberContent: Optional[str]
    sugarContent: Optional[str]
    servingSize: Optional[str]

class HowToStep(BaseModel):
    type_: Optional[str] = Field("HowToStep", alias='@type')
    text: str

class HowToSection(BaseModel):
    name: Optional[str]
    itemListElement: List[HowToStep]

class Author(BaseModel):
    type_: Optional[str] = Field("Person", alias='@type')
    name: str

class Recipe(BaseModel):
    context: Optional[str] = Field("https://schema.org", alias='@context')
    type_: Optional[str] = Field("Recipe", alias='@type')
    name: str
    description: Optional[str]
    image: Optional[Union[HttpUrl, List[HttpUrl]]]
    recipeYield: Optional[str]
    recipeIngredient: List[str]
    recipeInstructions: Optional[Union[List[HowToStep], List[HowToSection]]]
    prepTime: Optional[str]           
    cookTime: Optional[str]           
    totalTime: Optional[str]         
    recipeCategory: Optional[str]
    recipeCuisine: Optional[str]
    keywords: Optional[List[str]] 
    suitableForDiet: Optional[str]   
    nutrition: Optional[NutritionInformation]
    author: Optional[Author]
    video: Optional[HttpUrl]

class RecipeError(BaseModel):
    error: str
    missing_fields: Optional[List[str]]

class RecipeResponse(BaseModel):
    recipe: Optional[Recipe]
    suggested_version: Optional[Recipe]
    error_info: Optional[RecipeError]
