import os
import urllib.request as urlReq
import json
from time import sleep

def setURL (nextPage):
	sleep(4)
	global pageCount
	pageCount += 1
	if nextPage != '':
		crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&pageToken="+ nextPage +"&part=snippet&order=date&maxResults=" + str(SET_FETCH_LIMIT)
		getImg(crafted_youtube_url)
	else:
		crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&part=snippet&order=date&maxResults=" + str(SET_FETCH_LIMIT)
		getImg(crafted_youtube_url)

def getImg (uRL):
	requester = urlReq.build_opener()
	requester.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2311.135 Safari/537.36')]
	response = requester.open(uRL)
	y_json = response.read()
	global py_object
	py_object = json.loads(y_json)
	#Get the total number of videos in the channel
	for count, ob in enumerate(py_object['items']):
		itemType = ob['id']['kind']
		if itemType == 'youtube#video':
			videoID = ob['id']['videoId']
			count += 1
			# title of the video
			title = ob['snippet']['title']
			print('Downloading highres thumbnail for - '+title)
			try:
				resource = urlReq.urlopen("https://i.ytimg.com/vi/"+ videoID +"/sddefault.jpg")
			except:
				resource = urlReq.urlopen(ob['snippet']['thumbnails']['high']['url'])
			output = open("./thumbnails/"+ title +"-"+ str(pageCount) +"-"+ str(count) +".jpg","wb")
			output.write(resource.read())
			output.close()


if not os.path.exists('./thumbnails'):
    os.makedirs('./thumbnails')

#Ask for the youtube channels ID. You can get any channels ID. Refer to this link: https://support.google.com/youtube/answer/3250431
channel = input('Enter Channel ID: ')

fetch_limit = input('Max Results Per Page: (Not more than 50, default is 40) ')

if fetch_limit != "" and fetch_limit < 50:
    SET_FETCH_LIMIT = fetch_limit
else :
    SET_FETCH_LIMIT = 40

#Get the API key, you can get it from here 'https://developers.google.com/youtube/v3/getting-started'
API_KEY = input('Input your API-Key: ')
pageCount = 0
py_object = ''
setURL('')

while True:
	try:
		pageToken = py_object['nextPageToken']
	except:
		print('\n No next page \n')
		break
	else:
		print(pageToken)
		setURL(pageToken)