import logging
from weather import WeatherAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_30_day_forecast(api_key: str, city: str, units: str) -> None:
    """Fetch and print the 30-day weather forecast for a specified city."""
    weather_api = WeatherAPI(api_key)
    forecast_data = weather_api.get_weather_forecast(city, days=30, units=units)
    
    if forecast_data:
        logger.info(f"30-day forecast for {city}:")
        for day in forecast_data['list']:
            date = day['dt']  # Date in Unix time
            temperature = day['temp']['day']
            description = day['weather'][0]['description']
            print(f"Date: {date}, Temperature: {temperature}°C, Condition: {description.capitalize()}")
    else:
        print("No forecast data available.")
