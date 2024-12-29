import requests

# Ideal temperature, humidity, and rainfall conditions for each crop
crops_conditions = {
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

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={bangalore}&appid={ccc04b20b61a36cfa0362b1b2e656209}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to compare weather data with crop conditions
def compare_weather_with_crops(weather_data, crops_conditions):
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    rainfall = weather_data['rain']['1h'] if 'rain' in weather_data else 0  # Rainfall in the last hour

    advisory = {}

    for crop, conditions in crops_conditions.items():
        temp_status = "Suitable" if conditions["min_temp"] <= temp <= conditions["max_temp"] else "Unsuitable"
        humidity_status = "Suitable" if conditions["min_humidity"] <= humidity <= conditions["max_humidity"] else "Unsuitable"
        rainfall_status = "Suitable" if conditions["min_rainfall"] <= rainfall <= conditions["max_rainfall"] else "Unsuitable"

        advisory[crop] = {
            "Temperature": temp_status,
            "Humidity": humidity_status,
            "Rainfall": rainfall_status
        }

    return advisory

# Function to display crop advisories
def display_advisory(advisory):
    for crop, advice in advisory.items():
        print(f"\nAdvisory for {crop}:")
        for condition, status in advice.items():
            print(f"{condition}: {status}")

# Main function
def main():
    api_key = "ccc04b20b61a36cfa0362b1b2e656209"  # Replace with your OpenWeatherMap API key
    city = "Bangalore"  # You can change this to any city you wish to monitor

    # Fetch weather data from OpenWeatherMap
    weather_data = get_weather_data(bangalore, ccc04b20b61a36cfa0362b1b2e656209)

    # Compare weather data with crop conditions
    advisory = compare_weather_with_crops(weather_data, crops_conditions)

    # Display the advisory for each crop
    display_advisory(advisory)

# Run the main function
if __name__ == "__main__":
    main()
