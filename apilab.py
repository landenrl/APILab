from dotenv import load_dotenv
import os
import requests

#Load environment variables from the .env file
load_dotenv()

#Access environment variables
api_key = os.getenv('API_KEY')

base_url = 'http://api.openweathermap.org/data/2.5/'

def get_current_weather(city):
    weather_url = f"{base_url}weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']} degrees Celsius")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found or an error occurred.")