from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_current_weather(city="ankara", units = "metric"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data
#if console used
if __name__ == "__main__":
    city = input("Get weather conditions by city name \n")
    weather_data = get_current_weather(city)
    pprint(weather_data)
    
    
    
