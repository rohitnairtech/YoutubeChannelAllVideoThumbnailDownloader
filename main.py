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

#Build the GET request URL

crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&part=snippet,id&order=date&maxResults=" + str(SET_FETCH_LIMIT)

#Build URL opener and add header

import urllib.request as urlOpen

requester = urlOpen.build_opener()
requester.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2311.135 Safari/537.36')]

#Make the GET request

response = requester.open(crafted_youtube_url)

#Print the response header

print (response.info())

#Print response content (JSON)

y_json = response.read()

print(y_json)

#Convert JSON to Pythonic Object

import json

py_object = json.loads(y_json)

print(py_object)

#Iterate through newly converted py_object

for count, ob in enumerate(json_object['items']):
	count += 1
	print(ob)
	print(count)