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

def get_weather_forecast(city):
    forecast_url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(forecast_url)
    if response.status_code == 200:
        data = response.json()
        print(f"Forecast for {data['city]']['name']}:")
        for entry in data['list']:
            print(f"Date/Time: {entry['dt_txt']}")
            print(f"Temperature: {entry['main']['temp']} degrees Celsius")
            print(f"Weather: {entry['weather'][0]['description']}")
            print("-" * 20)
    else:
        print("City was not found or an error has occurred.")

def main():
    while True:
        city = input("Enter a city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        choice = input("What information would you like? (1: Current Weather, 2: Forecast): ").strip()
        if choice == '1':
            get_current_weather(city)
        elif choice == '2':
            get_weather_forecast(city)
        else:
            print("Invalid choice. Please select 1 or 2.")
if __name__ == "__main__":
    main()
        