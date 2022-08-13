# Create a Python Application which asks the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
# Display the weather forecast in a readable format to the user.
# Use comments within the application where appropriate in order to document what the program is doing.
# Use functions including a main function.
# Allow the user to run the program multiple times.
# Validate whether the user entered valid data. If valid data isn’t presented, notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Python 3.
# Use try blocks when establishing connections to the webservice.
# You must print a message to the user indicating whether the connection was successful.
import requests
import traceback
from colorama import init, Fore

init()

base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_Key = '8cc6a6f1fe6a424800c9efb35fbd4150'
print(Fore.BLUE + "This program establishes connection over the internet to display weather readings.")
city = input("Please type the name of your desired city or zipcode to get the Weather: \n")
url = base_url + "appid=" + API_Key + "&q=" + city
response = requests.get(url).json()


# fix this
def connect():
    try:
        requests.get(base_url)
        print("Connection Successful!")
    except Exception:
        print("Error Connecting")
        return connect()


def temp_maker(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


def temp2():
    temperature = response['main']['temp']
    temp_fahrenheit = temp_maker(temperature)
    if temp_fahrenheit <= 32:
        print(Fore.WHITE + f"The current temperature in {city.lower()} is {temp_fahrenheit:.1f}°")
    elif 33 < temp_fahrenheit <= 75:
        print(Fore.YELLOW + f"The current temperature in {city.lower()} is {temp_fahrenheit:.1f}°")
    elif temp_fahrenheit >= 75:
        print(Fore.LIGHTRED_EX + f"The current temperature in {city.lower()} is {temp_fahrenheit:.1f}°")
    else:
        print(Fore.BLUE + f"The current temperature in {city.lower()} is {temp_fahrenheit:.1f}°")


def humid():
    humidity = response['main']['humidity']
    if humidity <= 32:
        print(Fore.WHITE + f"The current humidity in {city.lower()} is {humidity:.1f}%")
    elif 33 < humidity <= 75:
        print(Fore.YELLOW + f"The current humidity in {city.lower()} is {humidity:.1f}%")
    elif humidity >= 75:
        print(Fore.LIGHTRED_EX + f"The current humidity in {city.lower()} is {humidity:.1f}%")
    else:
        print(Fore.BLUE + f"The current humidity in {city.lower()} is {humidity:.1f}%")


def feels_like():
    feels_like_k = response['main']['feels_like']
    feels_like_f = temp_maker(feels_like_k)
    if feels_like_f <= 32:
        print(Fore.WHITE + f"It feels like {feels_like_f:.1f}° in {city.lower()}")
    elif 33 < feels_like_f <= 75:
        print(Fore.YELLOW + f"It feels like {feels_like_f:.1f}° in {city.lower()}")
    elif feels_like_f >= 75:
        print(Fore.LIGHTRED_EX + f"It feels like {feels_like_f:.1f}° in {city.lower()}")
    else:
        print(Fore.BLUE + f"It feels like {feels_like_f:.1f}° in {city.lower()}")


def descript():
    description = response['weather'][0]['id']
    if 200 <= description <= 232:
        print(Fore.LIGHTYELLOW_EX + "Thu-Thu-Thunder")
    elif 300 <= description <= 321:
        print(Fore.LIGHTBLUE_EX + "Everyday I'm Drizzl'n")
    elif 500 <= description <= 531:
        print(Fore.BLUE + "Raindrops Keep Falling on My Head")
    elif 600 <= description <= 622:
        print(Fore.WHITE + "Let It Snow, Let It Snow, Let It Snow!")
    elif description == 800:
        print(Fore.LIGHTBLUE_EX + "Clear Skies!")
    elif description >= 801:
        print(Fore.LIGHTCYAN_EX + "Cloudy With a Chance of Meatballs")
    else:
        print(Fore.BLACK + "Your Insurance Won't Cover Damage From This Kind of Weather!")


def main():
    connect()
    temp2()
    humid()
    feels_like()
    descript()


if __name__ == '__main__':
    main()
