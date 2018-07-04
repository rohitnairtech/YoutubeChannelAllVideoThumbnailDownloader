import os
import urllib.request as urlReq
import json

if not os.path.exists('./thumbnails'):
    os.makedirs('./thumbnails')

#Ask for the youtube channels ID. Refer to this link: https://support.google.com/youtube/answer/3250431
channel = input('Enter Channel ID: ')

fetch_limit = input('Max Results Per Page: (Set to 40 If Left Blank) ')
DEFAULT_FETCH_LIMIT = 40

if fetch_limit != "" :
    SET_FETCH_LIMIT = fetch_limit
else :
    SET_FETCH_LIMIT = DEFAULT_FETCH_LIMIT

#Get the API key, you can get it from here 'https://developers.google.com/youtube/v3/getting-started'
API_KEY = input('Input your API-Key: ')

crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&part=snippet,id&order=date&maxResults=" + str(SET_FETCH_LIMIT)

requester = urlReq.build_opener()
requester.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2311.135 Safari/537.36')]

response = requester.open(crafted_youtube_url)

y_json = response.read()

py_object = json.loads(y_json)

for count, ob in enumerate(json_object['items']):
	itemType = ob['id']['kind']
	if itemType == 'youtube#video':
		count += 1
		print(ob['snippet']['title'])
		resource = urlReq.urlopen(ob['snippet']['thumbnails']['high']['url'])
		output = open("./thumbnails/thumbnail"+ str(count) +".jpg","wb")
		output.write(resource.read())
		output.close()