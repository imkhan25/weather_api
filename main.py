import argparse
import logging
import os
from weather import WeatherAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_arg_parser() -> argparse.ArgumentParser:
    """Builds and returns the argument parser."""
    parser = argparse.ArgumentParser(description="Simple Weather App")
    parser.add_argument(
        'city',
        type=str,
        help="City name for which to fetch the weather."
    )
    parser.add_argument(
        '-u', '--units',
        choices=['metric', 'imperial'],
        default='metric',
        help="Units for temperature. 'metric' for Celsius, 'imperial' for Fahrenheit."
    )
    return parser

def main() -> None:
    """Main entry point of the application."""
    parser = build_arg_parser()
    args = parser.parse_args()

    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        logger.error("Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return

    weather_api = WeatherAPI(api_key)
    weather_data = weather_api.get_weather(args.city, args.units)
    formatted_data = weather_api.format_weather_data(weather_data)
    print(formatted_data)

if __name__ == '__main__':
    main()
