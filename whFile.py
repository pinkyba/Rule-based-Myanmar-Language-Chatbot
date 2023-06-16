import re
import ismon
import isman

def search(data):
	open_file = ""
	if ismon.check(data):
		mon = '/home/pinky/chatbot-test/database/monstate/monFile'
		monname = open(mon,"r")
		monline = monname.readlines()
		for i in range(len(monline)):
			reg = monline[i].rstrip("\n").split("\t")
			if re.match(r'('+reg[0]+')',data):
				open_file = reg[1]
				break
		if open_file != "":
			print("Opened file in Mon folder: "+open_file)
			mon_cat = '/home/pinky/chatbot-test/database/monstate/'+open_file+''
			monopen = open(mon_cat,"r")
			mon_cat_line = monopen.readlines()
			return mon_cat_line
		else:
			print("Opened file in Mon folder: other")
			mon_cat = '/home/pinky/chatbot-test/database/monstate/other'
			monopen = open(mon_cat,"r")
			mon_cat_line = monopen.readlines()
			return mon_cat_line
	if isman.check(data):
		mdy = '/home/pinky/chatbot-test/database/mandalay/mdyFile'
		mdyname = open(mdy,"r")
		mdyline = mdyname.readlines()
		for i in range(len(mdyline)):
			reg = mdyline[i].rstrip("\n").split("/")
			if re.match(r'('+reg[0]+')',data):
				open_file = reg[1]
				break
		if open_file != "":
			print("Opened file in Mdy folder: "+open_file)
			mdy_cat = '/home/pinky/chatbot-test/database/mandalay/'+open_file+''
			mdyopen = open(mdy_cat,"r")
			mdy_cat_line = mdyopen.readlines()
			return mdy_cat_line
		else:
			print("Opened file in Mdy folder: other")
			mdy_cat = '/home/pinky/chatbot-test/database/mandalay/other'
			mdyopen = open(mdy_cat,"r")
			mdy_cat_line = mdyopen.readlines()
			return mdy_cat_line
				
	
