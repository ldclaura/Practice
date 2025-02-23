#--- imports ---
import requests
from twilio.rest import Client
from datetime import datetime, timedelta, date
import json
#--- sms ---

#--- stock ---
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#--- stock and news apis ---

stock_params = {
  "function" : "TIME_SERIES_DAILY",
  "symbol" : STOCK,
  "apikey" : ALPHAVANTAGE_API
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={ALPHAVANTAGE_API}"

TYPE_OF_NEWS = "stocks"
NEWS = f"https://newsapi.org/v2/everything?q={TYPE_OF_NEWS}&from=2024-12-29&sortBy=popularity&apiKey={NEWS_API}"
#---

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def save_alphavantage_data():
  """ I only have around 15 uses a day for the API so I needed to dump it all into a file """
  response = requests.get(url=ALPHAVANTAGE)
  response.raise_for_status
  print(response)
  data = response.json()
  try:
    timeseries = data["Time Series (Daily)"] #saves as variable (so get keyerror before file dump)
    with open("file.json", "w") as f: #file dump so if error next time will have latest data
      json.dump(data, f)
    return timeseries #data["Time Series (Daily)"]
  except KeyError: #if alphavantage api doesn't work because i've used it too much, use file instead.
    with open("file.json", "r") as f:
      strdata = f.read()
      jsonfile = json.loads(strdata) #so that its not textiowrapper type
      return jsonfile["Time Series (Daily)"] #data["Time Series (Daily)"]


def stock_increase_decrease(data):
  """When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News")."""
  current_date = date.today()
  yesterday_date = current_date - timedelta(days = 1)
  day_before_yesterday_date = yesterday_date - timedelta(days = 1)

  if str(yesterday_date) in data and str(day_before_yesterday_date) in data:
    yesterday_data = float(data[str(yesterday_date)]["4. close"])
    day_before_yesterday_data = float(data[str(day_before_yesterday_date)]["4. close"])
    print(yesterday_data)
    print(day_before_yesterday_data)
    checking_data = False
  else:
    checking_data = True
    while checking_data == True:
      yesterday_date = current_date - timedelta(days = +1)
      day_before_yesterday_date = yesterday_date - timedelta(days = 1)
      print(yesterday_date)


  percentage = ((yesterday_data - day_before_yesterday_data) / day_before_yesterday_data) * 100
  if percentage < 0:
    print(f"{percentage * - 1}% decrease")
    return percentage * - 1
  else:
    print(f"{percentage}% increase")
    return percentage
  #-------------------------------------

  
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


def save_news_data():
  """ I only have around 15 uses a day for the API so I needed to dump it all into a file """
  response = requests.get(url=NEWS)
  response.raise_for_status
  print(response)
  data = response.json()
  # with open ("news_file.json", "w") as f:
  #   json.dump(data, f)
  # thenews = []
  news1 = data["articles"][0]["title"]
  news2 = data["articles"][1]["title"]
  news3 = data["articles"][2]["title"]

  # for _ in range(3):
  #   thenews.append(data["articles"][_]["title"])
  #   thenews.append("\n")
  return news1 + "\n" + news2 + "\n" + news3
  #---
  # try:
  #   timeseries = data["Time Series (Daily)"] #saves as variable (so get keyerror before file dump)
  #   with open("news_file.json", "w") as f: #file dump so if error next time will have latest data
  #     json.dump(data, f)
  #   return timeseries #data["Time Series (Daily)"]
  # except KeyError: #if alphavantage api doesn't work because i've used it too much, use file instead.
  #   with open("news_file.json", "r") as f:
  #     strdata = f.read()
  #     jsonfile = json.loads(strdata) #so that its not textiowrapper type
  #     return jsonfile["Time Series (Daily)"] #data["Time Series (Daily)"]


print(ALPHAVANTAGE)
alph = save_alphavantage_data()
change_percentage = stock_increase_decrease(alph)
print(change_percentage)
somenews = save_news_data()
print(somenews)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message(percentage, news):
    
  client = Client(ACCOUNT_SID, AUTH_TOKEN)
  if percentage >= 5:
    bod = f"TSLA: 🔺{percentage}%"
  elif percentage <= -5:
    bod = f"TSLA: 🔻{percentage * - 1}%"
    
  # elif percentage > 0:
  #   bod = f"TSLA: 🔺{percentage}%"
  # elif percentage < 0:
  #   bod = f"TSLA: 🔻{percentage * - 1}%"

  message = client.messages.create(
    from_='+',
    body=f'{bod}\n{news}',
    to=MY_NUMBER
  )

  print(message.sid)

send_message(change_percentage, somenews)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

