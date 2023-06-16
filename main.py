import isman, ismon
import checksearch
import shortestpath
import searchGoogleHotel
import hotelSearch
import youtubeSearch
import youtube
import greetingCheck
import questagAll
import searchtag
import questag
import damerau_levenshtein
import array
import test
import downImg
import retrieveDict
import os
import random
import re
import shutil
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

f1=open("ques-mon","r")
f2=open("ans-mon","r")
f1line = f1.readlines()
f2line = f2.readlines()
f1len = len(f1line)

greet = [".*hello.*",".*hi.*",".*hey.*",".*ဟယ်လို.*",".*ဟဲလို.*",".*ဟလို.*","ဟိုင်း","ဟေး",".*မင်္ဂလာ.*ပါ.*"]
thank = [".*thankyou.*",".*thanks.*",".*thank.*",".*ကျေးဇူး.*"]
bye = ['.*bye.*','.*goodbye.*','.*seeyou.*','.*ဘိုင့်.*','.*ဘိုင်.*']
chatbot_name = ['.*(မင်း|နင့်)နာမည်.*','.*name.*']
fine = ['.*အဆင်ပြေ.*','.*နေကောင်း.*','.*ကောင်းပါ.*']
notfine = ['.*မပြေ.*','.*နေမကောင်း.*','.*မကောင်း.*','.*စိတ်ညစ်.*']

greet_res1 = ['မင်္ဂလာ နံနက်ခင်းလေး ပါ ခင်ဗျာ 😁️','မင်္ဂလာ နေ့လည်ခင်းလေး ပါ 🤗️','မင်္ဂလာ ညနေခင်းလေး ပါ ခင်ဗျာ 😊️','မင်္ဂလာ ညချမ်းလေး ပါ ခင်ဗျာ 🤗️']
greet_res = ['ဒီနေ့ နေကောင်းရဲ့လား ခင်ဗျ 🤗️','ဒီနေ့ အစစအရာ အဆင်ပြေ ရဲ့လား ခင်ဗျ 😊️']
thank_res = ['ရပါတယ် ဗျာ ....✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ကျေးဇူးတင် ပါ တယ် 🤗️','ဟုတ်ကဲ့ ။ ကျေးဇူးတင် ပါ တယ် ဗျ 😍️','ရပါတယ် ဗျာ .... ✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ဝမ်းသာ ပါ တယ် 😍️','ရပါတယ် ခင်ဗျ 🤗️ ပျော်ရွှင် သော နေ့လေး တစ်နေ့ ဖြစ်ပါစေ ....','ရပါတယ် ခင်ဗျ ပျော်စရာ နေ့လေး ဖြစ်ပါစေ ... 🤗️']
bye_res = ['Bye Bye ❤️','နှုတ်ဆက်ပါတယ် ခင်ဗျာ 🙂️','ဘိုင့်ဘိုင် 😍️','Good Bye 😍️']
bye_res1 = ['ပျော်ရွှင်ဖွယ်ကောင်းသော နေ့လေးတစ်နေ့ ဖြစ်ပါစေ ခင်ဗျာ ✌️','အခု လို လာရောက် မေးမြန်း တဲ့ အတွက် ကျေးဇူးတင်ပါတယ် 🤗️','တစ်နေ့တာ ပျော်ရွှင်ဖွယ်ရာ နေ့လေး ဖြစ် ပါစေ ❤️ ❤️','ကျွန်တော် အကြံပေးတာတွေ က လူကြီးမင်း အတွက် အထောက်အကူ ဖြစ်မယ် လို့ မျှော်လင့် ပါတယ် ခင်ဗျ 😀️']
kid = ['ဒီ မေးခွန်း ပဲ ခနခန မေးနေတယ် နော် .... နောက်နေတာလား 😝️ 😜️ 😜️ 😜️','ဒီ မေးခွန်း ကို မေး နေတာ ၂ ခါ ရှိ ပြီ နော် .... နောက်နေတာလား 😝️ 😜️ 😜️ 😜️']
name_res = ['ကျွန်တော့် နာမည် Travel bot လို့ ခေါ် ပါတယ် ခင်ဗျ 🖐️','ကျွန်တော့် နာမည် Travel bot ပါ 🤗️']
fine_res = ['ဟုတ်ကဲ့ ဝမ်းသာပါတယ် ဗျ 😊️','အခုလို သိရလို့ ဝမ်းသာပါတယ် ခင်ဗျ 🙂️','အခုလို ကြားရတာ ကျွန်တော် ဝမ်းသာပါတယ်ဗျာ ... 😀️']
fine_res1 = ['ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ အကူအညီ လိုအပ် ပါ သလဲ ခင်ဗျာ 😀️',
      'ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ များ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 😊️',
      'ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး အကူအညီ လိုအပ် နေ ပါ သလား 😀️',
      'ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ များ သိချင် ပါ သလဲ 😊️',
      'ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး အကြံဉာဏ် လိုအပ် နေ ပါ သလား 🤔️']
notfine_res = ['အခုလို ကြားရတာ စိတ်မကောင်းပါဘူး ခင်ဗျ 🙁️','အခုလို ကြားရတာ ဝမ်းနည်းပါတယ် ခင်ဗျ 😞️']
notfine_res1 = ['ကျွန်တော် ဘာ အကူအညီ ပေးရမလဲ ခင်ဗျာ ... ','ကျွန်တော် ဘာ များ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 🤗️','ရဲ့ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ များ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 😊️']

@app.route('/')
def chatbot():
	return render_template('login.html')
@app.route('/')
def logout():
	return render_template('chatbot.html')

@app.route('/login',methods = ['POST', 'GET'])
def loginresult():
	ch = 1
	if request.method == 'GET':
		return render_template("chatbot.html")
	if request.method == 'POST':
		del ques_arr[:]
		del box[:]
		name = request.form['name']
		password = request.form['pass']
		user = '/home/pinky/chatbot-test/user_cb/user'
		uFile = open(user,"r")
		uline = uFile.readlines()
		
		for i in range(len(uline)):
			split_line = uline[i].rstrip("\n").split("\t")
			if split_line[0] == name and split_line[1] == password:
				ch = 0
				break
			elif split_line[0] == name and split_line[1] != password:
				ch = 2
				break
			else:
				ch = 1
		
		if ch == 1:
			uFilew = open(user,"a+")
			uFilew.write(name+"\t"+password)
			uFilew.write("\n")
			return render_template("chatbot.html", uname = name)
		elif ch == 2:
			return render_template("login.html", msg = "Password is invalid !!")
		else:
			return render_template("chatbot.html", uname = name)
ques_arr = []
box = []
@app.route('/chatbot',methods = ['POST', 'GET'])
def chatresult():
	now = datetime.now()
	dist = 0
	maxdist = 0
	ck = 0
	mindist = 100
	qch = 1
	youtube_data = ""
	hotel = ""

	if request.method == 'GET':
		return render_template("chatresult.html")
	if request.method == 'POST':
		uname = request.form['uname']
		d= datetime.today()
		if d.hour >= 0 and d.hour < 12:
			time = uname+" ရေ ... "+greet_res1[0]
		elif d.hour >= 12 and d.hour < 16:
			time = greet_res1[1]+uname+" ရေ ... "
		elif d.hour >= 16 and d.hour < 19:
			time = uname+" ရေ ... "+greet_res1[2]
		else:
			time = uname+" ရေ ... "+greet_res1[3]
		print("user name1: "+uname)

		result = request.form
		for key, value in result.items():
			rmspace = value.replace(" ","")
			rmspace = rmspace.lower()
			
			grcheck = ""
			for gr in range(len(greet)):
				if re.match(greet[gr],rmspace):
					grcheck = "g"
					break
			for th in range(len(thank)):
				if re.match(thank[th],rmspace):
					grcheck = "t"
					break
			for by in range(len(bye)):
				if re.match(bye[by],rmspace):
					grcheck = "b"
					break
			for cn in range(len(chatbot_name)):
				if re.match(chatbot_name[cn],rmspace):
					grcheck = "n"
					break
			for fn in range(len(fine)):
				if re.match(fine[fn],rmspace):
					grcheck = "f"
					break
			for nf in range(len(notfine)):
				if re.match(notfine[nf],rmspace):
					grcheck = "nf"
					break
			print("greeting check: "+grcheck)
		### Check question is two time from user ###
			for qu in range(len(ques_arr)):
				if ques_arr[qu] == rmspace:
					qch = 0
					break
			if qch == 0 and grcheck != "g" and grcheck != "t" and grcheck != "b" and grcheck != "n" and grcheck != "nf":
				qkid = uname+" ရေ ... "+random.choice(kid)
				box.append([value])
				box.append([qkid])
				date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
				return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
			else:
				ques_arr.append(rmspace)
				#print(ques_arr)
			### Check user conversation is greeting, thank you, bye , name conversation ? ###
				if grcheck == "g":
					gres = uname+" "+random.choice(greet_res)
					box.append([value])
					box.append([time,gres]) 
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				elif grcheck == "t":
					gres = random.choice(thank_res)
					box.append([value])
					box.append([gres])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				elif grcheck == "b":
					gres = random.choice(bye_res)
					gres1 = random.choice(bye_res1)
					box.append([value])
					box.append([gres,gres1])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				elif grcheck == "n":
					gres = random.choice(name_res)
					box.append([value])
					box.append([gres])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				elif grcheck == "f":
					gres = random.choice(fine_res)
					gres1 = uname+" "+random.choice(fine_res1)
					box.append([value])
					box.append([gres,gres1])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				elif grcheck == "nf":
					gres = random.choice(notfine_res)
					gres1 = uname+" "+random.choice(notfine_res1)
					box.append([value])
					box.append([gres,gres1])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
			### Check General Coversation ####
				elif greetingCheck.greetCheck(rmspace):
					gc = greetingCheck.greetCheck(rmspace)
					box.append([value])
					box.append([gc])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				else:
					ques = array.city(rmspace)
					if ques == None:
						ques = "no"
					
					regPattern = [
					    r''+ques+'.*ထွက်ကုန်.*',
					    r''+ques+'.*လှေလှော်.*',
					    r''+ques+'.*ဆီမီး.*',
					    r''+ques+'.*လေ့လာ.*',
					    r''+ques+'.*ရေကူးကန်.*',
					    r''+ques+'.*ကားကြီးကွင်း.*',
					    r''+ques+'.*ဘုရားရှိခိုးကျောင်း.*',
					    r''+ques+'.*ခရစ်ယာန်ကျောင်း.*',
					    r''+ques+'.*အထိမ်းအမှတ်.*',
					    r''+ques+'.*အလည်အပတ်.*',
					    r''+ques+'.*ခရီးသွား.*ဘုရား.*',
					    r''+ques+'.*ခရီးသွား.*ရေတံခွန်.*',
					    r''+ques+'.*ခရီးသွား.*ကမ်းခြေ.*',
					    r''+ques+'.*ခရီးသွား.*',
					    r''+ques+'.*ဘာကား.*',
					    r''+ques+'.*ဘုရား.*',
					    r''+ques+'.*အဝေးပြေး.*',
					    r''+ques+'.*ထင်ရှား.*နေရာ.*',
					    r''+ques+'.*အထင်ကရ.*နေရာ.*',
					    r''+ques+'.*ဈေးချို.*ဆိုင်.*',
					    r''+ques+'.*ဈေးသက်.*ဆိုင်.*',
					    r''+ques+'.*ဈေးနည်း.*ဆိုင်.*',
					    r''+ques+'.*မြို့မဈေး.*',
					    r''+ques+'.*ဈေး.*',
					    r''+ques+'.*ဆွမ်းဆန်စိမ်း.*',
					    r''+ques+'.*ဆွမ်းကြီးလောင်း.*',
					    r''+ques+'.*တန်ဆောင်တိုင်.*',
					    r''+ques+'.*သင်္ကြန်.*'
					    r''+ques+'.*သွား.*တယ်.*',
					    r''+ques+'.*အနီး\s*တဝိုက်.*',
					    r''+ques+'.*တစ်ဆင့်.*', 
					    r''+ques+'.*တည်း.*',
					    r''+ques+'.*ပွဲ.*ဘယ်.*အချိန်.*',
					    r''+ques+'.*ဘာ.*ပွဲ.*',
					    r''+ques+'.*လူသွားလူလာ.*နေရာ.*',
					    r''+ques+'.*နေရာ.*လူသွားလူလာ.*',
					    r''+ques+'.*နာမည်ကြီး.*နေရာ.*',
					    r''+ques+'.*အဓိက.*',
					    r''+ques+'.*ဘုရား\s*ဖူး.*',
					    r''+ques+'.*တန်ခိုး\s*ကြီး.*',
					    r''+ques+'.*မြို့\s*အသီးသီး.*',
					    r''+ques+'.*ထင်ရှား.*ဘုရား.*',
					    r''+ques+'.*အထင်ကရ.*ဘုရား.*',
					    r''+ques+'.*နာမည်\s*ကြီး.*ဘုရား.*',
					    r''+ques+'.*ရိုးရာ\s*လက်မှု.*',
					    r''+ques+'.*လက်မှု.*လုပ်ကိုင်.*',
					    r''+ques+'.*လက်မှု.*',
					    r''+ques+'.*ဘာ\s*မြို့.*',
					    r''+ques+'.*အပန်း\s*ဖြေ.*နေရာ.*',
					    r''+ques+'.*ကမ်းခြေ\s*တွေ\s*ရှိ.*',
					    r''+ques+'.*ကမ်းခြေ.*လည်.*',
					    r''+ques+'.*နာမည်\s*ကြီး.*ကမ်းခြေ.*',
					    r''+ques+'.*လူသွား\s*လူလာ.*ကမ်းခြေ.*',
					    r''+ques+'.*အပန်း\s*ဖြေ.*ကမ်းခြေ.*',
					    r''+ques+'.*ရေတံခွန်.*ဘက်.*လည်',
					    r''+ques+'.*ကမ်းခြေ.*ဘက်.*လည်',
					    r''+ques+'.*ဘုရား.*ဘက်.*လည်',
					    r''+ques+'.*ဘက်.*လည်',
					    r''+ques+'.*ရေတံခွန်\s*တွေ\s*ရှိ.*',
					    r''+ques+'.*ရေတံခွန်.*လည်.*',
					    r''+ques+'.*နာမည်\s*ကြီး.*ရေတံခွန်.*',
					    r''+ques+'.*လူသွား\s*လူလာ.*ရေတံခွန်.*',
					    r''+ques+'.*အပန်း\s*ဖြေ.*ရေတံခွန်.*',
					    r''+ques+'.*တောင်\s*တက်\s*ခရီး.*',
					    r''+ques+'.*တောင်\s*တွေ\s*ရှိ.*',
					    r''+ques+'.*ရိုးရာ\s*အဝတ်\s*အထည်.*',
					    r''+ques+'.*ဘယ်.*သွားလည်.*',
					    r''+ques+'.*သွားလည်.*ဘယ်.*',
					    r''+ques+'.*သွားလည်.*',
					    r''+ques+'.*လည်\s*စရာ.*သိ.*',
					    r''+ques+'.*ဘယ်.*ဝေး.*',
					    r''+ques+'.*အနှံ့.*ဘယ်လောက်.*ကြာ.*',
					    r''+ques+'.*ဘယ်လောက်.*သွား.*',
					    r''+ques+'.*ဘယ်လောက်.*ကြာ.*',
					    r''+ques+'.*ဘယ်လောက်.*ယူ.*',
					    r''+ques+'.*အကွာအဝေး.*',
					    r''+ques+'.*ဘုန်းကြီး\s*ကျောင်း.*',
					    r''+ques+'.*ပြတိုက်.*',
					    r''+ques+'.*အပြင်.*ရှိ.*',
					    r''+ques+'.*မဖြစ်မနေ.*',
					    r''+ques+'.*ဂူ.*',
					    r''+ques+'.*ကစား\s*ကွင်း.*',
					    r''+ques+'.*ကလေး.*',
					    r''+ques+'.*ရာသီဥတု.*',
					    r''+ques+'.*လမ်းပန်းဆက်သွယ်ရေး.*',
					    r''+ques+'.*ဘာ\s*တွေ\s*ရှိ.*',
					    r''+ques+'.*ဘာ\s*တွေ\s*လုပ်.*',
					    r''+ques+'.*လက်ဆောင်.*',
					    r''+ques+'.*ဒေသထွက်ကုန်.*',
					    r''+ques+'.*ဒေသထွက်ပစ္စည်း.*',
					    r''+ques+'.*အမှတ်\s*တရ\s*ပစ္စည်း.*',
					    r''+ques+'.*တည်းခိုခန်း.*',
					    r''+ques+'.*ဟော်တယ်.*',
					    r''+ques+'.*ဘာ.*ထွက်.*',
					    r''+ques+'.*ရောင်း.*',
					    r''+ques+'.*ဝယ်.*',
					    r''+ques+'.*ဘာတွေရ.*',
					    r''+ques+'.*ရေ.*ကစား.*',
					    r''+ques+'.*ဘာ.*နဲ့.*',
					    r''+ques+'.*လည်\s*ပတ်.*',
					    r''+ques+'.*ဘယ်.*အလည်.*',
					    r''+ques+'.*အလည်.*ဘယ်.*',
					    r''+ques+'.*အ\s*လည်.*',
					    r''+ques+'.*ဘယ်\s*လို.*တက်.*',
					    r''+ques+'.*ဘယ်လို.*ပွဲ.*',
					    r''+ques+'.*ဘယ်\s*လို.*သွား.*',
					    r''+ques+'.*ဘယ်.*မှာ.*',
					    r''+ques+'.*ဘယ်နား.*',
					    r''+ques+'.*အစား.*',
					    r''+ques+'.*စားသောက်\s*ဆိုင်.*',
					    r''+ques+'.*ထမင်း\s*ဆိုင်.*',
					    r''+ques+'.*ကော်ဖီ\s*ဆိုင်.*',
					    r''+ques+'.*လက်ဖက်ရည်\s*ဆိုင်.*',
					    r''+ques+'.*ဝင်ကြေး.*',
					    r''+ques+'.*ဖူးချင်.*',
					    r''+ques+'.*ဒေသထွက်.*',
					    r''+ques+'.*ရေတံခွန်.*',
					    r''+ques+'.*ကမ်းခြေ.*',
					    r''+ques+'.*သဘာဝ.*',
					    r''+ques+'.*ရှိလား.*',
					    r''+ques+'.*လည်.*',
					    r''+ques+'.*သွားချင်.*',
					    r''+ques+'.*အသွားများ.*',
					    r''+ques+'.*သွား.*',
					    ]
					
					check = 0
					for r in range(len(regPattern)):
						if re.match(regPattern[r],rmspace):
							pattern = regPattern[r]
							check = 1
							break
					if check == 0:
						pattern = "no match"
					print(pattern)
					for i in range(f1len):
						f1line[i] = f1line[i].replace(" ","")
						f1line[i] = f1line[i].lower()
						if re.match(pattern,f1line[i]):
							print(pattern)
							print(i+1)
							box.append([value])
							box.append([f2line[i].rstrip("\n")])
							#print(box)
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							ck = 1
							return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
							
					print("If tue regex :"+str(ck))	
					if ck == 0:
						def searchGoogle(svalue):
							title = ""
							des = ""
							link = ""
							isdown = 1
									
							print("Google Search: "+svalue)
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
							letter = uname+"မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် google မှာ ဒါ ရှာတွေ့ ပါ တယ် ခင်ဗျာ 😃️ 😀️"
							box.append([value])
							box.append([title,des,link,image,letter])
							#print(box)
							return box

				####  Check dictionary ######
						dictData = retrieveDict.dictionary(rmspace)
						#print("Chatbot knowledge database: "+ dictData)
						if dictData != None:
							box.append([value])
							box.append([dictData])
							#print(box)
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				##### Check Shortest path ##########
						elif re.match(r'(.*အနီးဆုံး.*|.*လမ်း.*ဖြတ်.*|.*ဝင်လို့.*)',value) and re.match(r'(.*မဟာမြတ်မုနိ.*ကျောက်စိမ်းဘုရား.*|.*ကျောက်စိမ်းဘုရား.*မဟာမြတ်မုနိ.*)',value):
							if re.match(r'.*မဟာမြတ်မုနိ.*ကျောက်စိမ်းဘုရား.*',value):
								s1,s2 = shortestpath.search("မဟာမြတ်မုနိ", "ကျောက်စိမ်းဘုရား")
							elif re.match(r'.*ကျောက်စိမ်းဘုရား.*မဟာမြတ်မုနိ.*',value):
								s1,s2 = shortestpath.search("ကျောက်စိမ်းဘုရား", "မဟာမြတ်မုနိ")
							
							box.append([value])
							box.append([s1,s2])
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				#### Check is it question about Hotel ######
						elif re.match(r'(.*ဟိုတယ်.*|.*ဟော်တယ်.*|.*တည်းခိုခန်း.*|.*hotel.*|.*မိုတယ်.*|.*motel.*)',value):
							if ques != "no":
								ques = ques.replace('.*', '')
								hotel = ques+"+hotel"
								hbox = searchGoogleHotel.search(hotel,box,value)
								hletter = "hotel"
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = hbox, outLen = len(hbox), date = date, hletter = hletter, uname = uname)
							elif hotelSearch.search(rmspace):
								hotel = hotelSearch.search(rmspace)+"+hotel"
								hbox = searchGoogleHotel.search(hotel,box,value)
								hletter = "hotel"
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = hbox, outLen = len(hbox), date = date, hletter = hletter, uname = uname)
							else:
								cbox = searchGoogle(value)
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = cbox, outLen = len(cbox), date = date, uname = uname)			
																			
		###### Need segmentation ############
							
						else:
							cksearch = checksearch.tag(rmspace)
							#ck_arr = cksearch.split(" ")
							print("Check search tag: "+str(cksearch))
							if cksearch != None and isman.check(rmspace):		### Check user input is in noun dictionary < noun1 file> and is it for mdy conversation##
								print("Is it mdy? "+isman.check(rmspace))
								qtagAll = questagAll.tag(value)
								print("Question tag All (Mdy): "+qtagAll)
								all_ans = open("ans-mdy","r")
								ansline = all_ans.readlines()
								tag = '/home/pinky/chatbot-test/database/postag-mdy'
								tagFile = open(tag,"r")
								tagline = tagFile.readlines()
							### String Similarity for ques and ans #####
								for tag in range(len(tagline)):
									f1con = tagline[tag].rstrip("\n").split("/")

									distance = damerau_levenshtein.damerau(qtagAll,f1con[0])
									
									if distance < mindist:
										mindist = distance
										maxdata = ansline[tag]
									
								#print("maxdata"+maxdata)
								print("mindist ques mdy: "+str(mindist))
								if mindist <= 17:
									box.append([value])
									box.append([maxdata])
									#print(box)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
							
							if cksearch != None and ismon.check(rmspace): #### Is it for Mon Conversation #####
								print("Is it mon? "+ismon.check(rmspace))
								qtagAll = questagAll.tag(value)
								print("Question tag All(Mon): "+qtagAll)
								all_ans = open("ans-mon","r")
								ansline = all_ans.readlines()
								tag = '/home/pinky/chatbot-test/database/postag-mon'
								tagFile = open(tag,"r")
								tagline = tagFile.readlines()
							### String Similarity for ques and ans #####
								for tag in range(len(tagline)):
									f1con = tagline[tag].rstrip("\n").split("/")

									distance = damerau_levenshtein.damerau(qtagAll,f1con[0])
									
									if distance < mindist:
										mindist = distance
										maxdata = ansline[tag]
									
								#print("maxdata"+maxdata)
								print("mindist ques mon: "+str(mindist))
								if mindist <= 17:
									box.append([value])
									box.append([maxdata])
									#print(box)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
							if cksearch != None:
								maxdist = 0
								qtag = questag.tag(value)
								print("Question tag noun: "+qtag)
								
								qtmp1 = qtag.split(" ")
								#print(qtmp)

								tag1 = '/home/pinky/chatbot-test/database/postag-ans'
								tagFile = open(tag1,"r")
								tagline = tagFile.readlines()
								for tag in range(len(tagline)):
									f1con = tagline[tag].rstrip("\n").split("/")
									f1tmp = f1con[0].split(" ")
											
									dist = 0
									for qt in range(len(qtmp1)):
										for ft in range(len(f1tmp)):
											if qtmp1[qt] == f1tmp[ft]:
												dist += 1
												break
									if dist > maxdist:
										maxdist = dist
										maxdata = f1con[1]
								print("maxdist ans: "+str(maxdist))
								if maxdist >= 6:
									box.append([value])
									box.append([maxdata])
									#print(box)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)	
								elif re.match(r'(.*သွား.*|.*လမ်းညွှန်.*|.*ဘယ်နား.*)',rmspace):
									svalue = value.rstrip("။")
									gcheck = "ok"
									gmletter = "အခု "+uname+" မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် google map မှာ ဒါ ရှာတွေ့ ပါတယ် ခင်ဗျာ 😀️ အောက်က လင့်ခ် ကို နှိပ်ပြီး လမ်းကြောင်း ကို သိရှိနိုင်ပါတယ် ခင်ဗျာ ..."
									box.append([value])
									box.append([gmletter,svalue,gcheck])
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)	
									
								else:
									sbox = searchGoogle(qtag)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = sbox, outLen = len(sbox), date = date, uname = uname)
										
							elif re.match(r'(.*သွား.*|.*လမ်းညွှန်.*|.*ဘယ်နား*|.*ဝေး.*|.*ဘယ်မှာ.*)',rmspace):
								
								svalue = value.rstrip("။")
								gcheck = "ok"
								gmletter = "အခု "+uname+" မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် google map မှာ ဒါ ရှာတွေ့ ပါတယ် ခင်ဗျာ 😀️ အောက်က လင့်ခ်ကို နှိပ်ပြီး လမ်းကြောင်း ကို သိရှိနိုင်ပါတယ် ခင်ဗျာ ..."
								box.append([value])
								box.append([gmletter,svalue,gcheck])
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
							elif youtubeSearch.search(rmspace):
								youtube_search = youtubeSearch.search(rmspace)
								print("Youtube Search data: "+youtube_search)
								youtube_data = youtube.scrapeYoutube(youtube_search)
								ycheck = "youtube"
								youletter = "အခု "+uname+" မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် Youtube မှာ ဒီ ဗွီဒီယို လေး ရှာတွေ့ ပါတယ် ခင်ဗျာ ... အောက်က ဗွီဒီယို ကို click နှိပ် ပြီး ကြည့်နိုင် ပါတယ် ခင်ဗျ 😀️ 😀️"
								box.append([value])
								box.append([youletter,youtube_data,ycheck])
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
							else:
								cbox = searchGoogle(value)
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = cbox, outLen = len(cbox), date = date, uname = uname)

if __name__ == '__main__':
	app.run()

