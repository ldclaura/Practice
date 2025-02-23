import requests
from twilio.rest import Client

account_sid = ''
auth_token = ''
my_num = ''
twilio_phone = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17753208553',
  body='Hello dfdfdfdfdf',
  to=twilio_phone
)

print(message.sid)

#environment variables
#dir Env:
#prints Name and Value of environment variables
#security, separate where thigs are so that if u upload code u dont upload ur passwords n shit and paid api keys
#type in terminal export name_of_variable=value (no space between =)
#to use in pythonanywhere you need to do this then import os (so that u can use env variable)
#then variable = os.environ.get("name_of_variable")
#then go into scheduled tasks and add to command: export name_of_variable=value; export name_of_variable2=value; python3 main.py
#apilist.fun
