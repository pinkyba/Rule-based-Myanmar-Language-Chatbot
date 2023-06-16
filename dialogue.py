import re

def test(data):
	tmp = ""
	size = 0
	diag = '/home/pinky/chatbot-test/noun1'
	diagFile = open(diag,"r")
	diagline = diagFile.readlines()
	dlen = len(data)-2
	
	while(dlen >= size):
		for j in range(len(diagline)):
			tmp = diagline[j].rstrip("\n")
			if re.match(r'.*'+tmp+'.*',data[dlen].replace(" ","")):
				return tmp
		dlen -= 1
			
