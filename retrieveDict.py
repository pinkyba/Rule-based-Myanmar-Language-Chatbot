import re
import sys
import os

def dictionary(data):
	place = ""
	database = '/home/pinky/chatbot-test/database/dictionary/'
	files = os.listdir(database)
	for f in files:
		if re.match(r'.*'+f+'.*',data):
			place = f
	if place:
		path = '/home/pinky/chatbot-test/database/dictionary/'+place+''
		f1 = open(path,"r")
		line = f1.readlines()
		#print(len(line))
		for i in range(len(line)):
			linedata = line[i].split("/")
			if re.match(r'.*'+linedata[0]+'.*',data):
				return linedata[1]
				
		f1.close()
