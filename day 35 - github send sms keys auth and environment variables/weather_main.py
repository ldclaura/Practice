import os
import requests
from twilio.rest import Client

account_sid = '12345'
auth_token = '12345'
my_num = '+611232312'
twilio_phone = '+18234352'
client = Client(account_sid, auth_token)

ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
ENDPOINT2 = "https://api.openweathermap.org/data/2.5/forecast"
KEY = "123"
KEY2 = "123"
POSTCODE_LAT = "-12.3456"
POSTCODE_LONG = "12.34567"
#latlong.net
weather_params = {
    "lat" : POSTCODE_LAT,
    "lon" : POSTCODE_LONG,
    "appid" : KEY,
    "cnt" : 4
}
#"https://api.openweathermap.org/data/2.5/forecast?lat={POSTCODE_LAT}&lon={POSTCODE_LONG}&appid={KEY}"
response = requests.get(url=ENDPOINT2, params=weather_params)
response.raise_for_status
print(response)
weather_data = response.json()
#https://jsonviewer.stack.hu/






will_rain = False
for _ in range(0,len(weather_data)-1):
    condition = weather_data["list"][_]["weather"][len(weather_data["list"][_]["weather"])-1]["id"]
    print(condition)
    if condition < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
    from_='+',
    body='It will rain today',
    to=twilio_phone
    )
    print(message.sid)
else:
    message = client.messages.create(
    from_='+',
    body='It will not rain today',
    to=my_num
    )
    print(message.sid)
    # print(weather_data["list"][_]["weather"][0]["id"])
print(message.status)
# print(weather_data["list"][0]["weather"])
# print(weather_data["list"][1]["weather"])
# print(weather_data["list"][2]["weather"])
# print(weather_data["list"][3]["weather"])




#pythonanywhere:
#files
#upload files
#open file in pythonanywhere
#bash console here
#write in console python3 weather_main.py
#httpsconectionpool error
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
#older ver. is one yu used
#basically import http client, create proxy client, set http client param to proxy client
#the rest of it can stay the same
#get error
#scheduled tasks

#environment variables
#dir Env:
#prints Name and Value of environment variables
#security, separate where thigs are so that if u upload code u dont upload ur passwords n shit and paid api keys
#type in terminal export name_of_variable=value (no space between =)
#to use in pythonanywhere you need to do this then import os (so that u can use env variable)
#then variable = os.environ.get("name_of_variable")
#then go into scheduled tasks and add to command: export name_of_variable=value; export name_of_variable2=value; python3 main.py