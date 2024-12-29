import requests

def get_weather_data():
    api_key = "YOUR_API_KEY"
    city = "Bangalore"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={bangalore}&appid={ccc04b20b61a36cfa0362b1b2e656209}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

weather_data = get_weather_data()
print(weather_data)
