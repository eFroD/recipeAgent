from pydantic_evals.dataset import Case
from recipe_agent.models.output_models.recipe import Recipe


recipe_1 = {
  "@type": "Recipe",
  "cookTime": "PT17M",
  "totalTime": "PT17M",
  "description": "Ein leckerer Nudelauflauf mit Brokkoli, Schinken und Käse.",
  "name": "Brokkoli-Nudelauflauf",
  "suitableForDiet": "",
  "recipeIngredient": [
    "1 Brokkoli",
    "200 g Rigatoni",
    "1 Zwiebel, rot",
    "1 Peperoni, rot",
    "2 Knoblauchzehen",
    "2 Flocken Butter",
    "150 g Kochschinken",
    "Salz",
    "Pfeffer",
    "Muskat",
    "150 ml Sahne",
    "100 ml Kochwasser",
    "150 g Gouda"
  ],
  "video": "https://m.facebook.com/reel/1098675172447515/?referral_source=external_deeplink",
  "prepTime": "",
  "nutrition": {
    "servingSize": "",
    "fatContent": "",
    "calories": "",
    "carbohydrateContent": "",
    "proteinContent": "",
    "fiberContent": "",
    "sugarContent": ""
  },
  "recipeCategory": "Hauptgericht",
  "recipeInstructions": [
    {
      "@type": "HowToStep",
      "text": "Den Brokkoli vorbereiten: Röschen abschneiden. Ein Stück vom Strunk wegschneiden. Das Äußere vom Stielansatz wegschneiden und den Strunk vierteln."
    },
    {
      "text": "Den geviertelten Brokkoli-Strunk mit einer Portion Salz in einem Topf mit Deckel 5 Minuten kochen lassen.",
      "@type": "HowToStep"
    },
    {
      "@type": "HowToStep",
      "text": "Zwiebel und Knoblauch schälen und schneiden. Die rote Peperoni ebenfalls schneiden."
    },
    {
      "@type": "HowToStep",
      "text": "In einer Pfanne eine Flocke Butter schmelzen. Die geschnittenen Zwiebeln, Knoblauch und Peperoni dazugeben und anbraten."
    },
    {
      "text": "Die Nudeln zum kochenden Brokkoli-Strunk in den Topf geben, einen Deckel auflegen und weitere 3 Minuten kochen.",
      "@type": "HowToStep"
    },
    {
      "text": "Die Brokkoli-Röschen zu den Nudeln in den Topf geben, einen Deckel auflegen und 4 Minuten kochen.",
      "@type": "HowToStep"
    },
    {
      "text": "Den Kochschinken würfeln, falls gewünscht, und zu dem Gemüse in die Pfanne geben und schwenken.",
      "@type": "HowToStep"
    },
    {
      "@type": "HowToStep",
      "text": "Sobald die Nudeln 'mehr als al dente' sind, alles abgießen. Dabei das Kochwasser (ca. 100 ml) und den gekochten Brokkoli-Strunk in ein hohes Gefäß geben."
    },
    {
      "text": "Zum Strunk und der Flüssigkeit einen Schluck Sahne (insgesamt 150 ml) geben. Mit Salz, Pfeffer und Muskat würzen und alles pürieren, bis eine brokkoliartige Suppe entsteht.",
      "@type": "HowToStep"
    },
    {
      "@type": "HowToStep",
      "text": "Die abgetropften Nudeln und Brokkoli-Röschen zusammen mit dem angebratenen Gemüse (und Schinken) in eine Auflaufform geben und vermengen."
    },
    {
      "text": "Die pürierte Brokkolisauce über die Mischung in der Auflaufform gießen.",
      "@type": "HowToStep"
    },
    {
      "@type": "HowToStep",
      "text": "Den Auflauf mit geriebenem Gouda bestreuen."
    },
    {
      "text": "Das Ganze gratinieren. Gratinieren dauert 5 Minuten.",
      "@type": "HowToStep"
    }
  ],
  "recipeYield": "",
  "author": {
    "name": "Hannes / FOODBOOM",
    "@type": "Person"
  },
  "recipeCuisine": "Deutsch",
  "image": [],
  "@context": "https://schema.org",
  "keywords": [
    "Brokkoli",
    "Nudelauflauf",
    "Auflauf",
    "Pasta",
    "Schinken",
    "Käse"
  ]
}

cases = [Case(name="recipe_1", inputs="https://m.facebook.com/reel/1098675172447515/?referral_source=external_deeplink", expected_output=Recipe.model_validate(recipe_1))]
