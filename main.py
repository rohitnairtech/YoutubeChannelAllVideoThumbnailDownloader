#Check if a local directory with the name 'thumbnails' exists else create one
import os
if not os.path.exists('./thumbnails'):
    os.makedirs('./thumbnails')

#Ask for the youtube channels ID

channel = input('Enter Channel ID: ')

#Ask for the number of results that should be outputted if not answered then set default to 40

fetch_limit = input('Max Results Per Page: (Set to 40 If Left Blank) ')
DEFAULT_FETCH_LIMIT = 40

if fetch_limit != "" :
    SET_FETCH_LIMIT = fetch_limit
else :
    SET_FETCH_LIMIT = DEFAULT_FETCH_LIMIT

#Get the API key, you can get it from here 'https://developers.google.com/youtube/v3/getting-started'

API_KEY = input('Input your API-Key: ')


