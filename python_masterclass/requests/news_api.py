import requests

api_key = "pub_24ef48753f724b2fbb54c334321e7d2f"
url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q=coffee"

response = requests.get(url)
content = response.json()

for article in content['results']:
    title = article['title']
    description = article['description']
    print(title)
    print(description)
