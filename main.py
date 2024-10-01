import argparse
import logging
import os
from forecast_10_days import get_10_day_forecast
from forecast_30_days import get_30_day_forecast

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
    parser.add_argument(
        '--forecast',
        choices=['10', '30'],
        help="Specify the number of days for the forecast. '10' for 10-day, '30' for 30-day."
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

    if args.forecast == '10':
        get_10_day_forecast(api_key, args.city, args.units)
    elif args.forecast == '30':
        get_30_day_forecast(api_key, args.city, args.units)
    else:
        current_weather = WeatherAPI(api_key).get_current_weather(args.city, args.units)
        formatted_data = WeatherAPI.format_weather_data(current_weather)
        print(formatted_data)

if __name__ == '__main__':
    main()
