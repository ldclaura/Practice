#python datetime strftime()
#apis and making post requests
#authorization headers
#environment variables

#---------------------------------------------------------------------------
# 2. [OPTIONAL] In order to be able to post our workout data while we're out and about, it would be easier if we can access the console and run the code in a browser.

# We can do this using Repl.it

# This is a free tool but requires email signup. So it's completely optional if you want to do this. It's not so much for learning Python, but it would be cool to have this "app" accessible from a web browser on mobile.

# Step 1: Sign up for a free account on https://replit.com/

# Step 2: Create a new Repl and name it Google-Workouts
#------------------------------------------------------------------------------------
#$ENV:APP_ID="ah" sets environment variable (to do in terminal)          
#echo $ENV:APP_ID tells you if environment variable exists/is set do in terminal
import os
import requests
from datetime import date, datetime
APP_ID = os.environ["APP_ID"]
# APP_ID = ""
# os.environ["APP_ID"] = APP_ID
API_KEY = os.environ["API_KEY"]

# os.environ["API_KEY"] = API_KEY
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
# SHEET_ENDPOINT = "https://api.sheety.co/bcopyOfMyWorkouts/workouts"
# os.environ["SHEET_ENDPOINT"] = SHEET_ENDPOINT
TOKEN = os.environ["TOKEN"]
# TOKEN = 
# os.environ["TOKEN"] = TOKEN
GENDER = "female"
WEIGHT = 42
HEIGHT = 157
AGE = 20
today = date.today().strftime("%d/%m/%Y")
current_time = datetime.now().time().strftime("%I:%M")
#nutritionix password = 
#application id = 
#application keys = 
link = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheetylink = "https://api.sheety.co//copyOfMyWorkouts/workouts"
#https://api.uat.syndigo.com/api/auth?username=YourApiUsername&secret=YourUrlEncodedSecret

query = input("What was your exercise?: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
sheetyheader = {
    "Authorization" : f"Basic {TOKEN}"
}

author = {

}
params = {
    "query" : query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=link, json=params, headers=headers) #headers=headers NOT header=header
result = response.json()
print(result)
print(result["exercises"][0]["nf_calories"])

sheetyparams = {
    "workout" : 
    {
    "date" : str(today),
    "time" : str(current_time),
    "exercise" : str(result["exercises"][0]["user_input"]),
    "duration" : float(result["exercises"][0]["duration_min"]),
    "calories" : float(result["exercises"][0]["nf_calories"])
    }
}


sheetyresponse = requests.post(url=sheetylink, json=sheetyparams, headers=sheetyheader)
print(sheetyresponse.raise_for_status)
# response.raise_for_status
test = sheetyresponse.json()

# thing = requests.get(url=sheetylink)

# data = response.json()

