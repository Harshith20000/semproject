document.getElementById('getWeather').addEventListener('click', function() {
    // Get the city name entered by the user
    const city = document.getElementById('city').value;
    
    // If no city is entered, prompt the user to enter a valid city
    if (!city) {
        alert('Please enter a city name.');
        return;
    }

    // Fetch the weather data from the API (use your backend or a public weather API)
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${bangalore}&appid=ccc04b20b61a36cfa0362b1b2e656209&units=metric`)
        .then(response => response.json())
        .then(data => {
            // Extract the necessary information from the API response
            const temperature = data.main.temp;
            const humidity = data.main.humidity;
            const weatherDescription = data.weather[0].description;
            const rainfall = data.rain ? data.rain['1h'] : 0; // If rainfall data exists
            
            // Display the weather details on the page
            document.getElementById('weatherDetails').innerHTML = `
                <h4>Weather in ${city}</h4>
                <p><strong>Temperature:</strong> ${temperature}°C</p>
                <p><strong>Humidity:</strong> ${humidity}%</p>
                <p><strong>Weather:</strong> ${weatherDescription}</p>
                <p><strong>Rainfall (last hour):</strong> ${rainfall} mm</p>
                <h5>Crop Advisory:</h5>
                <p>${generateCropAdvice(temperature, humidity, rainfall)}</p>
            `;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            alert('Error fetching weather data. Please try again later.');
        });
});

// Function to generate crop advice based on the weather
function generateCropAdvice(temperature, humidity, rainfall) {
    // Crop weather preferences for different crops
    const idealConditions = {
        rice: { temp: { min: 22, max: 32 }, humidity: { min: 80 }, rainfall: { min: 1500 } },
        maize: { temp: { min: 18, max: 30 }, humidity: { min: 60 }, rainfall: { min: 500, max: 800 } },
        groundnut: { temp: { min: 20, max: 30 }, humidity: { min: 60 }, rainfall: { min: 300, max: 600 } },
        cotton: { temp: { min: 25, max: 35 }, humidity: { min: 50 }, rainfall: { min: 300, max: 600 } }
    };

    // Evaluate the weather conditions and give crop advice
    let advice = 'The weather is suitable for growing crops, but we need to check more details.';

    if (temperature >= idealConditions.rice.temp.min && temperature <= idealConditions.rice.temp.max &&
        humidity >= idealConditions.rice.humidity.min && rainfall >= idealConditions.rice.rainfall.min) {
        advice = 'Rice is well-suited for this weather.';
    } else if (temperature >= idealConditions.maize.temp.min && temperature <= idealConditions.maize.temp.max &&
        humidity >= idealConditions.maize.humidity.min && rainfall >= idealConditions.maize.rainfall.min) {
        advice = 'Maize is a good choice for this weather.';
    } else if (temperature >= idealConditions.groundnut.temp.min && temperature <= idealConditions.groundnut.temp.max &&
        humidity >= idealConditions.groundnut.humidity.min && rainfall >= idealConditions.groundnut.rainfall.min) {
        advice = 'Groundnut can grow well under these conditions.';
    } else if (temperature >= idealConditions.cotton.temp.min && temperature <= idealConditions.cotton.temp.max &&
        humidity >= idealConditions.cotton.humidity.min && rainfall >= idealConditions.cotton.rainfall.min) {
        advice = 'Cotton is suitable for this weather.';
    }

    return advice;
}
