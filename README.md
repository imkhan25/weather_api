# Simple Weather App

A simple Python application to fetch weather data from OpenWeatherMap API.

## Features

- Fetch current weather for a city.
- Specify temperature units (Celsius or Fahrenheit).

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
   git clone https://github.com/imkhan25/simple_weather_app.git
   cd simple_weather_app
   
2.Install dependencies:

pip install -r requirements.txt

3. Set your OpenWeatherMap API key:

export OPENWEATHERMAP_API_KEY='your_api_key_here'  # On Unix or Mac
set OPENWEATHERMAP_API_KEY='your_api_key_here'  # On Windows

Usage
Run the application:

For a 10-day forecast:
python main.py London --forecast 10 -u metric
For a 30-day forecast:

python main.py London --forecast 30 -u metric
For current weather:

python main.py London
