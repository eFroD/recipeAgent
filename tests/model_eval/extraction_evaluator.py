from pydantic_evals.evaluators import Evaluator, EvaluatorContext
from pydantic_evals.dataset import Dataset
from recipe_agent.models.output_models.recipe import Recipe
from recipe_agent.agents.description_validator import recipe_validator
from tests.model_eval.eval_dataset import cases
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logfire
import os
logfire_token = os.environ.get("LOGFIRE_WRITE_TOKEN")
logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()


model = SentenceTransformer('all-MiniLM-L6-v2')

class IngredientsSimilarityEvaluator(Evaluator[Recipe, Recipe]):
    def evaluate(self, ctx: EvaluatorContext[Recipe, Recipe]) -> float:
        expected_ingredients = " ".join(ctx.expected_output.recipeIngredient)
        actual_ingredients = " ".join(ctx.output.recipeIngredient)
        emb_exp = model.encode([expected_ingredients])
        emb_act = model.encode([actual_ingredients])
        sim = cosine_similarity(emb_exp, emb_act)[0][0]
        
        return sim 

class InstructionsSimilarityEvaluator(Evaluator[Recipe, Recipe]):
    def evaluate(self, ctx: EvaluatorContext[Recipe, Recipe]) -> float:
        excpected_instructions = " ".join([step.text for step in ctx.expected_output.recipeInstructions])
        actual_instructions = " ".join([step.text for step in ctx.output.recipeInstructions])
        emb_exp = model.encode([excpected_instructions])
        emb_act = model.encode([actual_instructions])
        sim = cosine_similarity(emb_exp, emb_act)[0][0]
       
        return sim

class MandatoryFieldsEvaluator(Evaluator[Recipe, Recipe]):
    def evaluate(self, ctx: EvaluatorContext[Recipe, Recipe]) -> float:
        recipe = ctx.output
        mandatory = ['name', 'recipeIngredient', 'type_', 'context']
        missing = [f for f in mandatory if not getattr(recipe, f, None)]
        return 1.0 if not missing else 0.0

class CompletenessEvaluator(Evaluator[Recipe, Recipe]):
    def evaluate(self, ctx: EvaluatorContext[Recipe, Recipe]) -> float:
        recipe = ctx.output
        has_ingredients = bool(recipe.recipeIngredient)
        has_instructions = bool(recipe.recipeInstructions and len(recipe.recipeInstructions) > 0)
        return 1.0 if has_ingredients and has_instructions else 0.0
    
dataset = Dataset(cases=cases, evaluators=[MandatoryFieldsEvaluator(), CompletenessEvaluator(), IngredientsSimilarityEvaluator(), InstructionsSimilarityEvaluator()])

def call_agent(input_data):
    output = recipe_validator.run_sync(f"Please extract the recipe from the given url: {input_data}. The target language is de")
    recipe = Recipe.model_validate(output.output.recipe)
    return recipe

report = dataset.evaluate_sync(call_agent)
report.print(include_input=True, include_output=False)
