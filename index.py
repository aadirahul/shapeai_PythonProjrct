from ctypes.wintypes import CHAR
from re import S
import requests
#import os
from datetime import datetime
import json

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# print ("-------------------------------------------------------------")
# print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
# print ("-------------------------------------------------------------")

# print ("Current temperature is: {:.2f} deg C".format(temp_city))
# print ("Current weather desc  :",weather_desc)
# print ("Current Humidity      :",hmdt, '%')
# print ("Current wind speed    :",wind_spd ,'kmph')

#printing weather data in a txt file.
with open("Weather.txt" , "w+") as f:
    f.write('-------------------------------------------------------------')
    f.write('\n')
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write('\n')
    f.write("-------------------------------------------------------------")
    f.write('\n')
    f.write("Current temperature is: {:.2f} deg C".format(temp_city))
    f.write('\n')
    f.write("Current weather desc {} :" .format(weather_desc))
    f.write('\n')
    f.write("Current Humidity {} %  :".format(hmdt))
    f.write('\n')
    f.write("Current wind speed  {} kmph :".format(wind_spd) )
    f.write('\n')
