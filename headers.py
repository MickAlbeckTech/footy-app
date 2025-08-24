import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "text/plain"})

print(f"Your request for the url {url} yielded response code {response.status_code}")

print(response.text)