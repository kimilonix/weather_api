import requests
import json

api_key = "YOUR_API_KEY"
city_name = input("Enter city name : ")

complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]

    z = x["weather"]
    weather_description = z[0]["description"]

    print(f"Temperature (in kelvin unit) = {current_temperature}")
    print(f"atmospheric pressure (in hPa unit) = {current_pressure}")
    print(f"humidity (in percentage) = {current_humidity}")
    print(f"description = {weather_description}")
else:
    print(" City Not Found ")
