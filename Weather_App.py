
import requests

def get_weather(api_key, city):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # url = "https://www.google.com/search?q="+"weather"+city

    base_url = "http://api.openweathermap.org/data/2.5/weather?" 
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    
    response = requests.get(complete_url)
    return response.json()    

def display_current_weather(data):
    if data["cod"] == 200:
        print(f"Weather in {data["name"]}:")
        print(f"Temperature: {int(data["main"]["temp"])-273.15}°C")
        print(f"Current Pressure(in hPa unit): {data["main"]["pressure"]}")
        print(f"Humidity: {data["main"]["humidity"]}%")
        print(f"Weather: {data["weather"][0]["description"]}")
    else:
        print("City not found. Please try again.")


def main():
    api_key = "4dd1bfc3465ee3efb2bdbfefb7b348f7"
    api_key = "2b2974487c3e211a19781fe2ef39cf1b"
    city = input("Enter city name: ")

    # Get and Display current weather
    current_weather_data = get_weather(api_key=api_key, city=city)
    display_current_weather(current_weather_data)

if __name__ == "__main__":
    main()