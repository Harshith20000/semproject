crops = {
    "Tomato": {"min_temp": 20, "max_temp": 30, "min_humidity": 60, "max_humidity": 80},
    "Rice": {"min_temp": 22, "max_temp": 30, "min_rainfall": 500, "max_rainfall": 2000},
}

def advisory(weather_data):
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    advice = []

    for crop, conditions in crops.items():
        if temp < conditions["min_temp"] or temp > conditions["max_temp"]:
            advice.append(f"Temperature is unsuitable for {crop}.")
        if humidity < conditions["min_humidity"] or humidity > conditions["max_humidity"]:
            advice.append(f"Humidity is unsuitable for {crop}.")
        
    return advice

print(advisory(weather_data))
