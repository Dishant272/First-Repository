import win32com.client as os  # this fix for all audio output

import requests
import json

speak = os.Dispatch("SAPI.SpVoice")  # this is requires for audio

city = input("Enter the name of the city:")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
# print(r.text)
# print(type(r.text))
wdic = json.loads(r.text)
print(f"your city '{city}' temperature is:", wdic["current"]["temp_c"])
w = wdic["current"]["temp_c"]

speak.Speak(f"The current weather in {city} is {w} degrees")

# make by myself
z = wdic["location"]["localtime"]
speak.Speak(f"The current weather in {city}  time is {z}")
