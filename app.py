import requests

API_KEY = "YOUR_API_KEY_HERE"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != 200:
    print("City not found!")
else:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Report")
    print("------------------")
    print(f"City: {city}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")
