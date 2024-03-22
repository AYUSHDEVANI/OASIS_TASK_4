
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
