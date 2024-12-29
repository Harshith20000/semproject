# Crop database with weather preferences and growing stages
crop_database = {
    "Rice": {
        "weather_preferences": {
            "temperature": {"min": 20, "max": 35},
            "humidity": {"min": 70, "max": 85},
            "rainfall": {"min": 1000, "max": 1500}
        },
        "growing_stages": {
            "sowing": "Rice is planted in flooded fields, which requires water management.",
            "vegetative": "The plant grows rapidly, requiring abundant water and moderate temperatures.",
            "flowering": "Rice flowers; consistent water supply is crucial for grain development.",
            "maturity": "The crop reaches full grain maturity. The field can be flooded to prevent weeds."
        }
    },
    "Maize": {
        "weather_preferences": {
            "temperature": {"min": 18, "max": 32},
            "humidity": {"min": 60, "max": 75},
            "rainfall": {"min": 500, "max": 800}
        },
        "growing_stages": {
            "sowing": "Maize seeds are planted when the soil temperature is above 18°C.",
            "vegetative": "Rapid growth stage where the maize requires plenty of sunlight and moderate rain.",
            "flowering": "The plant flowers and pollinates. Water availability is critical during this phase.",
            "maturity": "Maize reaches full maturity. Reduced water needs after the flowering stage."
        }
    },
    "Groundnut": {
        "weather_preferences": {
            "temperature": {"min": 20, "max": 35},
            "humidity": {"min": 50, "max": 60},
            "rainfall": {"min": 400, "max": 600}
        },
        "growing_stages": {
            "sowing": "Groundnuts are planted in warm soil with well-drained conditions.",
            "vegetative": "The plant grows with moderate water and sunlight, avoiding excess moisture.",
            "flowering": "Flowers emerge, requiring warm conditions and consistent moisture.",
            "maturity": "The pods mature and start to dry; careful management of water is necessary to avoid fungal diseases."
        }
    },
    "Cotton": {
        "weather_preferences": {
            "temperature": {"min": 25, "max": 35},
            "humidity": {"min": 50, "max": 60},
            "rainfall": {"min": 500, "max": 800}
        },
        "growing_stages": {
            "sowing": "Cotton seeds are planted after the last frost when the temperature is above 20°C.",
            "vegetative": "The plant grows rapidly with plenty of sunlight and moderate rainfall.",
            "flowering": "Cotton flowers bloom. This is the crucial stage for boll formation.",
            "maturity": "The bolls mature, and cotton is ready for harvest. Water should be reduced after flowering."
        }
    }
}

# Function to print crop information
def print_crop_info(crop_name):
    if crop_name in crop_database:
        crop_info = crop_database[crop_name]
        print(f"\nCrop: {crop_name}")
        
        # Weather preferences
        print("Weather Preferences:")
        print(f"Temperature: {crop_info['weather_preferences']['temperature']['min']}°C to {crop_info['weather_preferences']['temperature']['max']}°C")
        print(f"Humidity: {crop_info['weather_preferences']['humidity']['min']}% to {crop_info['weather_preferences']['humidity']['max']}%")
        print(f"Rainfall: {crop_info['weather_preferences']['rainfall']['min']} mm to {crop_info['weather_preferences']['rainfall']['max']} mm")
        
        # Growing stages
        print("\nGrowing Stages:")
        for stage, description in crop_info["growing_stages"].items():
            print(f"{stage.capitalize()}: {description}")
    else:
        print(f"{crop_name} is not available in the database.")

# Example: Display crop information for Rice, Maize, Groundnut, and Cotton
print_crop_info("Rice")
print_crop_info("Maize")
print_crop_info("Groundnut")
print_crop_info("Cotton")
