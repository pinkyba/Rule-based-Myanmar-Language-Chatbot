import urllib.request
from bs4 import BeautifulSoup


def scrapeYoutube(data):
	youtube_link = []
	query = urllib.parse.quote(data)
	url = "https://www.youtube.com/results?search_query="+query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		line = vid['href'].replace('/watch?v=', '')
		youtube_link.append(line)
		
	return youtube_link[0]
