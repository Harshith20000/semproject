import requests

# Define the ideal conditions for crops
crops = {
    "Rice": {
        "min_temp": 25, "max_temp": 35,
        "min_humidity": 70, "max_humidity": 85,
        "min_rainfall": 1000, "max_rainfall": 1500
    },
    "Maize": {
        "min_temp": 20, "max_temp": 30,
        "min_humidity": 60, "max_humidity": 75,
        "min_rainfall": 500, "max_rainfall": 800
    },
    "Groundnut": {
        "min_temp": 25, "max_temp": 35,
        "min_humidity": 50, "max_humidity": 60,
        "min_rainfall": 400, "max_rainfall": 600
    },
    "Cotton": {
        "min_temp": 25, "max_temp": 35,
        "min_humidity": 50, "max_humidity": 60,
        "min_rainfall": 500, "max_rainfall": 800
    }
}

# Fetch weather data from OpenWeatherMap API
def get_weather_data(bangalore, ccc04b20b61a36cfa0362b1b2e656209
):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Compare current weather with crop's ideal conditions
def compare_weather_with_crops(weather_data, crops):
    current_temp = weather_data['main']['temp']
    current_humidity = weather_data['main']['humidity']
    current_rainfall = weather_data['rain']['1h'] if 'rain' in weather_data else 0  # rainfall in last 1 hour

    advisory = {}

    for crop, conditions in crops.items():
        temp_advice = "Suitable" if conditions["min_temp"] <= current_temp <= conditions["max_temp"] else "Unsuitable"
        humidity_advice = "Suitable" if conditions["min_humidity"] <= current_humidity <= conditions["max_humidity"] else "Unsuitable"
        rainfall_advice = "Suitable" if conditions["min_rainfall"] <= current_rainfall <= conditions["max_rainfall"] else "Unsuitable"

        advisory[crop] = {
            "Temperature": temp_advice,
            "Humidity": humidity_advice,
            "Rainfall": rainfall_advice
        }

    return advisory

# Display the advisory for each crop
def display_advisory(advisory):
    for crop, advice in advisory.items():
        print(f"\nAdvisory for {crop}:")
        for condition, status in advice.items():
            print(f"{condition}: {status}")

# Main function
def main():
    api_key = "ccc04b20b61a36cfa0362b1b2e656209"
  # Replace with your actual OpenWeatherMap API key
    city = "Bangalore"
    
    # Fetch current weather data
    weather_data = get_weather_data(bangalore, ccc04b20b61a36cfa0362b1b2e656209)
    
    # Compare weather with ideal crop conditions
    advisory = compare_weather_with_crops(weather_data, crops)
    
    # Display the advisory
    display_advisory(advisory)

# Run the main function
if __name__ == "__main__":
    main()
