import requests

API_Key = "5d31bd840e9c45e629661ca4b33f967b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from API"""
    params = {
        "q": city,
        "appid": API_Key,
        "units": "metrics" #Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temp_k = data["main"]["temp"]
        feels_k = data["main"]["feels_like"]

        temp_c = temp_k - 273.15
        feels_c = feels_k - 273.15
        weather = data['weather'][0]['description']
        print(f"\nWeather in {city_name}")
        print(f"Temperature: {temp_c:.2f}°C (feels like {feels_c:.2f}°C)")
        print(f"Condition: {weather.capitalize()}")
    else:
        print("\nCould not fetch weather data. Check city name or API Key.")


def main():
    print("--- Weather App ---")
    while True:
        city = input("\nEnter city name (or type Exit to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)



if __name__ == "__main__":
    main()