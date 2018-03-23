import requests
import json

apikey="0ab54f33d38b117ed34839a6f924c90b"

cities=["Seoul,KR","Tokyo,JP","New York,US"]

api="http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
k2c= lambda k: k -273.15

for name in cities:
    url = api.format(city=name,key=apikey)

    r= requests.get(url)
    print(url)

    data=json.loads(r.text)

    print("+ CITY =", data["name"])
    print("| WEATHER =",data["weather"][0]["description"])
    print("| MIN TEMP =",k2c(data["main"]["temp_min"]))
    print("| Max TEMP =",k2c(data["main"]["temp_max"]))
    print("| HUMIDITY =",data["main"]["humidity"])
    print("| PRESSURE =",data["main"]["pressure"])
    print("| DEG =",data["wind"]["deg"])
    print("| SPEED =",data["wind"]["speed"])
    print("")
 
 
