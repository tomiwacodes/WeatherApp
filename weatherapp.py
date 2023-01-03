import requests
API_Key = "62c0e03460ead63b7d59f9e1912c55e2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = f"{BASE_URL}?appid={API_Key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    print("Weather: ", weather)
    temperature = (data["main"]["temp"])*1.8 -459.67
    print("Temperature: ", temperature, "Degrees Fahrenheit")
else:
    print("An error occured")
