from recipe_agent.integrations.mealie_integration import push_recipe_to_mealie
import requests

test_json = {
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Blumenkohlsteak mit goldener Grana Padano Kruste, cremigem Bohnenpüree und Tomaten-Kräuter-Dressing",
  "description": "Blumenkohlsteak mit goldener Grana Padano Kruste, cremigem Bohnenpüree und einem frischen Tomaten-Kräuter-Dressing. Gesund, proteinreich und voller Geschmack. Die Kombination aus Butterbohnen & Grana Padano liefert hochwertiges Eiweiß, Kalzium und sättigt ohne Schwere. Grana Padano ist von Natur aus laktosefrei und passt perfekt in eine ausgewogene, moderne Küche.",
  "image": "https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/522819255_18519012295046223_5891187172040965353_n.jpg?stp=dst-jpg_e15_fr_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDE5MjAuc2RyLmY4Mjc4Ny5kZWZhdWx0X2NvdmVyX2ZyYW1lLmMyIn0&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEkG3rSkhM6oLxPtemyGdvPvKkx-YhXfvm17rH3qY0F7jWceWx6RNUDILU45TQu5xe0bibQjULguOeHX6gtUL4L&_nc_ohc=9fn3kysl0KsQ7kNvwG3gmGk&_nc_gid=H25x0gOyd-B4ysT7yAU9VQ&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_Afdn0lI-B9Tdk2ncSIQWgIkkD5MtleXzl_atzDkvBOLmLw&oe=68EE9998&_nc_sid=d885a2",
  "recipeYield": "2 Personen",
  "recipeIngredient": [
    "1 Kopf Blumenkohl (die Abschnitte können auch mit der Marinade gebacken oder für Suppen oder Pürees verwendet werden)",
    "Ca. 50 g Grana Padano",
    "20 ml Olivenöl",
    "1 TL Paprika edelsüß",
    "Pfeffer aus der Mühle",
    "Salz",
    "1 Schalotte",
    "1 Knoblauchzehe",
    "1 Dose weiße Bohnen (400 g)",
    "1 Zweig Thymian",
    "Ca. 100 ml Gemüsebrühe",
    "Jeweils 1 Handvoll Petersilie und Basilikum",
    "1 Tomate",
    "Etwas Zitronenabrieb und ein Spritzer Zitronensaft",
    "Ca. 20 ml Olivenöl (für das Dressing)",
    "Salz, Pfeffer"
  ],
  "recipeInstructions": [
    {
      "@type": "HowToStep",
      "text": "Blumenkohl in zwei schöne Steaks schneiden."
    },
    {
      "@type": "HowToStep",
      "text": "Grana Padano reiben."
    },
    {
      "@type": "HowToStep",
      "text": "Eine Marinade aus 20 ml Olivenöl, 1 TL edelsüßem Paprika und Pfeffer anrühren. Salz wird später hinzugefügt."
    },
    {
      "@type": "HowToStep",
      "text": "Die Blumenkohlsteaks mit der Marinade gut bedecken und auf ein Backblech legen. Die restliche Marinade darüber verteilen und dann salzen, um eine gleichmäßigere Verteilung zu erreichen."
    },
    {
      "@type": "HowToStep",
      "text": "Eine Seite der Steaks in den Grana Padano tauchen und mit der Käseseite nach unten auf das Backblech legen."
    },
    {
      "@type": "HowToStep",
      "text": "Die Steaks im vorgeheizten Backofen bei 200 °C Ober-/Unterhitze für 20 Minuten backen."
    },
    {
      "@type": "HowToStep",
      "text": "Für das Bohnenpüree Schalotte und Knoblauch klein schneiden und in Olivenöl anschwitzen."
    },
    {
      "@type": "HowToStep",
      "text": "Einen Zweig Thymian dazugeben und mit Gemüsebrühe ablöschen."
    },
    {
      "@type": "HowToStep",
      "text": "Weiße Bohnen hinzufügen, mit Salz und Pfeffer abschmecken und alles pürieren."
    },
    {
      "@type": "HowToStep",
      "text": "Für das Dressing Petersilie, Basilikum, gehäutete und entkernte Tomate, Zitronenabrieb und Zitronensaft mit Olivenöl vermengen und mit Salz und Pfeffer abschmecken."
    }
  ],
  "prepTime": "PT15M",
  "cookTime": "PT20M",
  "totalTime": "PT35M",
  "recipeCategory": "Hauptgericht",
  "recipeCuisine": "italienisch",
  "keywords": [
    "Blumenkohlsteak",
    "Grana Padano",
    "Bohnenpüree",
    "Tomaten-Kräuter-Dressing",
    "gesund",
    "proteinreich"
  ],
  "suitableForDiet": "laktosefrei",
  "author": {
    "@type": "Person",
    "name": "thomas.kocht"
  },
  "video": "https://www.instagram.com/reel/DMXyVFysZeB/?utm_source=ig_web_copy_link",
  "url": "https://www.instagram.com/reel/DMXyVFysZeB/?utm_source=ig_web_copy_link"
}

async def test():
     await push_recipe_to_mealie(test_json)
import os
MEALIE_API_KEY = os.environ.get("MEALIE_API_KEY", None)
if __name__ == "__main__":
   test()