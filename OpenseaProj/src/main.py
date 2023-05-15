# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:48:58 2023

@author: joaquin
"""


import requests

api_key = "7b712a06a86444feb98e5fd4269eb83c"

url = "https://api.opensea.io/api/v1/assets"
# url = "https://api.opensea.io/v2/assets"

params = {"limit": 3} # Change limit to desired amount of listings to retrieve

# Add the API key to the header
headers = {"X-API-KEY": api_key}



# Make the request and get the JSON response
response = requests.get(url, params=params, headers=headers)
data = response.json()



# # Extract the listings from the response
listings = data["assets"]

# Loop through the listings and print some details
for listing in listings:
    # print(listing)
    temp = listing['collection']
    temp2 = temp['name']
    # print(temp2)
    
    print("----\n\n\n")



