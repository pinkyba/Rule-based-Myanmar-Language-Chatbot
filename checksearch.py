import re
tmp = ""
def tag(data):
	
	cityFile = open("noun1","r")
	cityline = cityFile.readlines()
	for i in range(len(cityline)):
		tmp = cityline[i].rstrip("\n")
		if re.match(r'.*'+tmp+'.*',data):
			return tmp
