import os
import urllib.request as urlReq
import json
from time import sleep
# for video download
import youtube_dl
ydl = youtube_dl.YoutubeDL({'outtmpl': './video/%(title)s.%(ext)s'})

def setURL (nextPage):
	sleep(2)
	global pageCount
	pageCount += 1
	if nextPage != '':
		crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&pageToken="+ nextPage +"&part=snippet&order=date&maxResults=" + str(SET_FETCH_LIMIT)
	else:
		crafted_youtube_url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + channel + "&part=snippet&order=date&maxResults=" + str(SET_FETCH_LIMIT)
	processUrl(crafted_youtube_url)
	
def processUrl (uRL):
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
			title = ob['snippet']['title']
			count += 1
			if content_type == 1:
				getVideo (title, videoID)
			elif content_type == 2:
				altUrl = ob['snippet']['thumbnails']['high']['url']
				getImg (title, videoID, altUrl, count)
			elif content_type == 3:
				getTitle (title)


def getVideo (title, videoID):
	print('Downloading video title - '+title)
	try:
		ydl.download(['https://www.youtube.com/watch?v='+videoID])
	except:
		print('Some error while downloading')
	else:
		sleep(4)

def getTitle (title):
	global title_text
	title_text += title + '\n'

def getImg (title, videoID, altUrl, count):
	print('Downloading highres thumbnail for - '+title)
	try:
		resource = urlReq.urlopen("https://i.ytimg.com/vi/"+ videoID +"/sddefault.jpg")
	except:
		resource = urlReq.urlopen(altUrl)
	output = open("./thumbnails/"+ title +"-"+ str(pageCount) +"-"+ str(count) +".jpg","wb")
	output.write(resource.read())
	output.close()




#Ask for the youtube channels ID. You can get any channels ID. Refer to this link: https://support.google.com/youtube/answer/3250431
channel = input('Enter Channel ID: ')

fetch_limit = input('Max Results Per Page: (Not more than 50, default is 40) ')

if fetch_limit != "" and fetch_limit < 50:
    SET_FETCH_LIMIT = fetch_limit
else :
    SET_FETCH_LIMIT = 40

#Get the API key, you can get it from here 'https://developers.google.com/youtube/v3/getting-started'
#default thumbnail
API_KEY = input('Input your API-Key: ')

title_text = ''

content_type = input('What do you want to Download? \n 1: Video \n 2: Thumbnail \n 3: Titles \n (Respond with only the number, default is thumbnail) \n Your response? : ')

if (content_type == '1' or content_type == '2' or content_type == '3'):
	content_type = int(content_type)
else:
	content_type = 2

if content_type == 2:
	if not os.path.exists('./thumbnails'):
		os.makedirs('./thumbnails')

pageCount = 0
py_object = ''
setURL('')

while True:
	try:
		pageToken = py_object['nextPageToken']
	except:
		print('\n No next page \n')
		if content_type == 3:
			output = open("./titles.txt","w")
			output.write(title_text)
			output.close()
		break
	else:
		print(pageToken)
		setURL(pageToken)