import requests

url = "http://127.0.0.1:8000/recipes/extract-recipe"
payload = {
    "url": "https://www.instagram.com/reel/DMXyVFysZeB/?utm_source=ig_web_copy_link",
    "target_language": "german",
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
