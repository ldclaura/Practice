import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 0.0 # Your latitude
MY_LONG = -0.0 # Your longitude
lat_test = 54.507351
long_test = -5.127758


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
#time: 2024-12-10 13:02:18.143931
current_hour = time_now.hour
test_hour = 6
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def compare_positions():
    """ True means you can see ISS """
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        #if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        #^^^ this one is just easier to understand, im not sure what abs means n does ^^^
        if current_hour >= sunrise and current_hour <= sunset: #day
            return False
        else: #night
            return True
    else:
        return False

def send_email(from_email, from_password, to_email):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_email, password=from_password)
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f"""ISS is currently visible!!!\nThe coordinates of the ISS are:\nLatitude: {iss_latitude}\nLongitude: {iss_longitude}""")
    except:
        print("Failed")
    finally:
        print("COMPLETED")

program_on = True
while program_on == True:
    see_iss = compare_positions()
    if see_iss == True:
        send_email(my_email, password, email_to)
    else:
        pass
    time.sleep(60)

