#get requests.get()
#post requests.post()
#put requests.put()
#delete requests.delete()

#post to twitter post to google sheets
#update values in spreadsheet put
#delete data in twitter

import requests
import datetime as dt
from datetime import date
USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token" : TOKEN, #password
    "username" : USERNAME, #https://pixe.la/@lauralaura29
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
graph_config = {
    "id" : "graph1",
    "name" : "My Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ichou",
}
graph_pixel_config = {
    #DO NOT INCLUDE GRAPHID
    #ALL VALUES STRING
    "date" : str(date.today().strftime("%Y%m%d")),
    "quantity" : "5",
}
graph_pixel_config2 = {
    #DO NOT INCLUDE GRAPHID
    #ALL VALUES STRING
    "quantity" : "5",
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{str(date.today().strftime('%Y%m%d'))}"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) #KWAARGS
# response2 = requests.post(url=pixel_endpoint, json=graph_pixel_config, headers=headers) #KWAARGS
# response3 = requests.put(url=put_pixel_endpoint, json=graph_pixel_config2, headers=headers) #KWAARGS
response4 = requests.delete(url=put_pixel_endpoint, json=graph_pixel_config2, headers=headers)
print(response4.text)