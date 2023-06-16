import downImg
import test
import os
import shutil
import re
import random

def search(svalue,hbox,hvalue):
	title = ""
	des = ""
	link = ""
	isdown = 1
									
	print("Hotel Search: "+svalue)
	data = test.scrap(svalue)
	#print(data)
	static = '/home/pinky/chatbot-test/static/img/'
	files = os.listdir(static)
	for f in files:
		if f == svalue:
			isdown = 0
	if isdown == 1:
		img = downImg.image(svalue)
										
	for i in range(len(data)):
		if title == "" and data[i]['title'] != None:
			title = data[i]['title']
											
		if des == "" and data[i]['description'] != None:
			des = data[i]['description']
											
		if link == "" and data[i]['link'] != None and re.match(r'https://.*',data[i]['link']):
			link = data[i]['link']
									
	down = '/home/pinky/chatbot-test/downloads/'
	static = '/home/pinky/chatbot-test/static/img/'
	files = os.listdir(down)
						
	for f in files:
		shutil.move(down+f, static)
	path = 'static/img/'+svalue+'/' 
	files = os.listdir(path)
	img = random.choice(files)
	image = svalue+'/'+img
	hotel = svalue.replace('+hotel', '')
	letter = hotel+" မှာ ရှိတဲ့ ဟိုတယ်/တည်းခိုခန်း တွေကို ကျွန်တော် ရှာထားပေးပါတယ် ခင်ဗျ အောက်က လင့်ခ်ထဲမှာ ဝင်ကြည့်ပါနော် 😃️ 😀️"
	hbox.append([hvalue])
	hbox.append([title,des,svalue,image,letter])
	return hbox
