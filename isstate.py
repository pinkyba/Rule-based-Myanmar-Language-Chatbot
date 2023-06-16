import re

def search(data):
	tmp = ""
	city = '/home/pinky/chatbot-test/search/is_state'
	cityFile = open(city,"r")
	cityline = cityFile.readlines()
	for i in range(len(cityline)):
		tmp = cityline[i].rstrip("\n")
		if re.match(r'.*'+tmp+'.*',data):
			print("data in is-state: "+tmp)
			return True
