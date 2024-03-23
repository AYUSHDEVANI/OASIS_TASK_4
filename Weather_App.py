
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()    

def display_current_weather(data):
    if data["cod"] == 200:
        print(f"Weather in {data["name"]}:")
        print(f"Temperature: {data["main"]["temp"]}°C")
        print(f"Humidity: {data["main"]["humidity"]}%")
        print(f"Weather: {data["weather"][0]["description"]}")
    else:
        print("City not found. Please try again.")

def get_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def display_forecast(data):
    if data["cod"] == 200:
        print(f"Forecast for {data["city"]["name"]}:")
        for forecast in data["list"]:
            print(f"Date: {forecast["dt_txt"]}, Temperature: {forecast["main"]["temp"]}°C, Weather: {forecast["weather"][0]["description"]}")

    else:
        print("City not found, Please try again.")

def main():
    api_key = "4dd1bfc3465ee3efb2bdbfefb7b348f7"
    city = input("Enter city name: ")

    # Get and Display current weather
    current_weather_data = get_weather(api_key=api_key, city=city)
    display_current_weather(current_weather_data)

    # Get and Display Forecast
    forecast_data = get_forecast(api_key=api_key, city=city)
    display_forecast(forecast_data)


