import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

# Endpoint to create a new user
pixela_endpoint = "https://pixe.la/v1/users"

# New user API parameters
user_params = {
    "token" : TOKEN, 
    "username" : USERNAME, 
    "agreeTermsOfService" : "yes", 
    "notMinor" : "yes",   
}

# Create a new user
response = requests.post(url=pixela_endpoint, json=user_params)
# Print out HHTP response code
print(response.text)   
                                                                       
# Endpoint to create a graph
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# New graph API parameters
graph_config = {
    "id" : "graph1" ,
    "name": "Distance walked" ,
    "unit": "Km" , 
    "type": "float" , 
    "color": "momiji" , # color is in japanese which means yellow
}

# Creating a HTTP header 
headers = {
    "X-USER-TOKEN": TOKEN,
}

GRAPH_ID = graph_config['id']

# Create a graph
response = requests.post(url=create_graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Posting a value to the graph
# Create a new pixel in habit tracker 
graph_value_endpoint = f"{create_graph_endpoint}/{GRAPH_ID}"

# New pixel API parameters
yesterday = datetime(year=2022, month=2, day=2)
today = datetime.now()

# To gat a day the datetime object can be formatted as datetime(year=200 , month=7, day=23)
# Formatting the date into a string using the strftime() method
print
pixel_config = {
    "date": yesterday.strftime("%Y%m%d") , 
     "quantity": "30", 
 }

# Create a new pixel 
pixel_1_config = {
    "date": today.strftime("%Y%m%d") , 
    "quantity": "50", 
}

# Create an endpoint to update pixel data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "80"
}

response = requests.post(url=graph_value_endpoint , json=pixel_config, headers=headers)
response = requests.post(url=graph_value_endpoint , json=pixel_1_config, headers=headers)
print(response.text)

# Update pixel using put method 
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Create an endpoint to delete pixel 
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Delete pixel using delete method 
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)