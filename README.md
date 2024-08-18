## weather_api
### A simple Python script to fetch and display weather information for a given city using the OpenWeatherMap API.

## Usage
### To use this script, simply run it and enter the city name when prompted:
```
python weather_api.py
Enter city name: <city_name>
```
### Replace <city_name> with the actual city name you want to fetch weather information for.

## Requirements
### 1- Python 3.x
### 2- requests library (install with pip install requests)
### 3- OpenWeatherMap API key (sign up for a free account on OpenWeatherMap.org)
## How it works
### The script sends a GET request to the OpenWeatherMap API with the city name and API key. The API response is parsed as JSON and the following weather information is extracted:

1. Temperature (in Kelvin)
2. Atmospheric pressure (in hPa)
3. Humidity (in percentage)
3. Weather description
### The script then prints out the extracted weather information.

## API Key
### You'll need to replace the api_key variable with your own OpenWeatherMap API key. You can obtain a free API key by signing up on OpenWeatherMap.org.

## Note
### This script uses the free tier of the OpenWeatherMap API, which has limitations on the number of requests per day. Be sure to review the API terms and conditions before using this script in production.
### The temperature is returned in Kelvin by default. If you want to display it in Celsius or Fahrenheit, you'll need to modify the script accordingly.

