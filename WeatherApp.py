import datetime as dt
import json, requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"

API_Key = '8cc6a6f1fe6a424800c9efb35fbd4150'
city = input("Please type the name of your city to get the Weather! \n")

url = base_url + "appid=" + API_Key + "&q=" + city


def temp_maker(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


response = requests.get(url).json()
temperature = response['main']['temp']
temp_fahrenheit = temp_maker(temperature)
print(f"The current temperature in {city} is {temp_fahrenheit:.2f}°")

if __name__ == '__main__':
    pass
