import requests
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str, units: str = 'metric') -> Optional[dict]:
        """Fetch the weather data for a specified city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units
        }
        try:
            logger.info(f"Fetching weather data for {city}.")
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"An error occurred: {err}")
        return None

    @staticmethod
    def format_weather_data(data: dict) -> str:
        """Format the weather data into a human-readable string."""
        if data:
            city = data.get("name")
            country = data.get("sys", {}).get("country")
            temperature = data.get("main", {}).get("temp")
            weather_description = data.get("weather", [{}])[0].get("description")
            formatted_data = (f"Weather in {city}, {country}:\n"
                              f"Temperature: {temperature}°C\n"
                              f"Condition: {weather_description.capitalize()}")
            return formatted_data
        return "No weather data available."
