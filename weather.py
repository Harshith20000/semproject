import requests

# Replace YOUR_API_KEY with the actual API key you obtained
api_key = "ccc04b20b61a36cfa0362b1b2e656209"
city = "Bangalore"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)

