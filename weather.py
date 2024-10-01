import requests
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city: str, units: str = 'metric') -> Optional[dict]:
        """Fetch the current weather data for a specified city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units
        }
        try:
            logger.info(f"Fetching current weather data for {city}.")
            response = requests.get(f"{self.base_url}/weather", params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"An error occurred: {err}")
        return None

    def get_weather_forecast(self, city: str, days: int, units: str = 'metric') -> Optional[dict]:
        """Fetch the weather forecast data for a specified city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units,
            'cnt': days  # Number of days (for 10-day or 30-day)
        }
        try:
            logger.info(f"Fetching {days}-day weather forecast for {city}.")
            response = requests.get(f"{self.base_url}/forecast/daily", params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"An error occurred: {err}")
        return None

    @staticmethod
    def format_weather_data(data: dict) -> str:
        """Format the current weather data into a human-readable string."""
        if data:
            city = data.get("name")
            country = data.get("sys", {}).get("country")
            temperature = data.get("main", {}).get("temp")
            weather_description = data.get("weather", [{}])[0].get("description")
            formatted_data = (f"Current weather in {city}, {country}:\n"
                              f"Temperature: {temperature}°C\n"
                              f"Condition: {weather_description.capitalize()}")
            return formatted_data
        return "No weather data available."
