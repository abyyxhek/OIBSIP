import requests

API_KEY =  "ba13a824af001af73098b72c189749cb"  # 🔁 Replace this with your real API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print("\n🌍 Weather in:", data['name'])
        print("🌡️ Temperature:", data['main']['temp'], "°C")
        print("💧 Humidity:", data['main']['humidity'], "%")
        print("🌤️ Condition:", data['weather'][0]['description'].capitalize())
        print("💨 Wind Speed:", data['wind']['speed'], "m/s")
    else:
        print("❌ City not found or invalid API key.")

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
