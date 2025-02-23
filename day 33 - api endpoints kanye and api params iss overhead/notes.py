#application programming interfaces (API)
#an API is a set of commands functions protocols and objects that programmers can use to create software or interact iht an external system
import requests
from datetime import datetime
# MY_LAT = 
# MY_LONG = 
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #Response [200]

#Response [404] <-- thing you're looking for doesn't exist
#Response [1xx] <-- hold on, somethings happening this is not final
#Response [2xx] <-- worked and all good
#Response [3xx] <-- go away no permission
#Response [4xx] <-- you screwed up
#Response [5xx] <-- i screwed up (website down??)

response.raise_for_status() #for errors.
data = response.json()
timestamp = response.json()["timestamp"]
iss_position = response.json()["iss_position"]
print(data) #{'iss_position': {'longitude': '', 'latitude': ''}, 'message': 'success', 'timestamp': 1733619962}
longitude = data["iss_position"]["longitude"]
print(longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
#API Parameters !!! 
sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#
print(sun) #400?
print("sunrise")
sunrise = sun.json()["results"]["sunrise"]
splitsunrise = sunrise.split("T")[1].split(":")[0] #sunrise hour
print(splitsunrise)
print("sunset")
sunset = sun.json()["results"]["sunset"]
splitsunset = sunset.split("T")[1].split(":")[0] #sunset hour
print(splitsunset)
#https://api.sunrise-sunset.org/json

time_now = datetime.now()
print("currenttime")
print(time_now.hour)