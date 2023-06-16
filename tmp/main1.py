import whFile, dialogue, isstate
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
chatbot_name = ['.*(မင်း|နင့်).*နာမည်.*','.*name.*']
fine = ['.*အဆင်ပြေ.*','.*နေကောင်း.*','.*ကောင်းပါ.*']
notfine = ['.*မပြေ.*','.*နေမကောင်း.*','.*မကောင်း.*','.*စိတ်ညစ်.*']

greet_res1 = ['မင်္ဂလာ နံနက်ခင်းလေး ပါ ခင်ဗျာ 😁️','မင်္ဂလာ နေ့လည်ခင်းလေး ပါ 🤗️','မင်္ဂလာ ညနေခင်းလေး ပါ ခင်ဗျာ 😊️','မင်္ဂလာ ညချမ်းလေး ပါ ခင်ဗျာ 🤗️']
greet_res = ['ဒီနေ့ နေကောင်းရဲ့လား ခင်ဗျ 🤗️','ဒီနေ့ အစစအရာ အဆင်ပြေ ရဲ့လား ခင်ဗျ 😊️']
thank_res = ['ရပါတယ် ဗျာ ....✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ကျေးဇူးတင် ပါ တယ် 🤗️','ဟုတ်ကဲ့ ။ ကျေးဇူးတင် ပါ တယ် ဗျ 😍️','ရပါတယ် ဗျာ .... ✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ဝမ်းသာ ပါ တယ် 😍️','ရပါတယ် ခင်ဗျ 🤗️ ပျော်ရွှင် သော နေ့လေး တစ်နေ့ ဖြစ်ပါစေ ....','ရပါတယ် ခင်ဗျ 🤗️ ပျော်စရာ နေ့လေး ဖြစ်ပါစေ .... 🤗️']
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
			##### Check for each mdy and mon file with category with damerau similarity #######
				cksearch = checksearch.tag(rmspace) #### Check is it in (noun1) dictionary >> noun1 = is_mon+is_man ####
				print("Check search tag: "+str(cksearch)) 
				is_state = isstate.search(rmspace)
				print("Check is state: "+str(is_state)) 
			####  Check dictionary ######
				if cksearch != None and retrieveDict.dictionary(rmspace):
					dictData = retrieveDict.dictionary(rmspace)
					box.append([value])
					box.append([dictData])
					#print(box)
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)

				if cksearch != None and whFile.search(rmspace):
					whfile = whFile.search(rmspace)
						
					qtagAll = questagAll.tag(value.lower())
					print("Question tag All: "+qtagAll)
					qtagAll = qtagAll.replace(" ","")
						
					for tag in range(len(whfile)):
						f1con = whfile[tag].rstrip("\n").split("/")
						distance = damerau_levenshtein.damerau(qtagAll,f1con[0].replace(" ",""))
						if distance < mindist:
							mindist = distance
							maxdata = f1con[2]

					print("mindist ques distance: "+str(mindist))
					if mindist <= 12:
						box.append([value])
						box.append([maxdata])
						#print(box)
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				

				if cksearch != None:																		
						
					if re.match(r'(.*အနီးဆုံး.*|.*လမ်း.*ဖြတ်.*|.*ဝင်လို့.*)',value) and re.match(r'(.*မဟာမြတ်မုနိ.*ကျောက်စိမ်းဘုရား.*|.*ကျောက်စိမ်းဘုရား.*မဟာမြတ်မုနိ.*)',value):
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
							
						if hotelSearch.search(rmspace):
							hotel = hotelSearch.search(rmspace)+"+hotel"
							hbox = searchGoogleHotel.search(hotel,box,value)
							hletter = "hotel"
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							return render_template("chatresult.html", out = hbox, outLen = len(hbox), date = date, hletter = hletter, uname = uname)
						else:
							cbox = searchGoogle(value)
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							return render_template("chatresult.html", out = cbox, outLen = len(cbox), date = date, uname = uname)
					elif re.match(r'(.*သွား.*|.*လမ်းညွှန်.*|.*ဘယ်နား.*)',rmspace):
						svalue = rmspace.rstrip("။")
						gcheck = "ok"
						gmletter = "အခု "+uname+" မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် google map မှာ ဒါ ရှာတွေ့ ပါတယ် ခင်ဗျာ 😀️ အောက်က လင့်ခ် ကို နှိပ်ပြီး လမ်းကြောင်း ကို သိရှိနိုင်ပါတယ် ခင်ဗျာ ..."
						box.append([value])
						box.append([gmletter,svalue,gcheck])
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
												
					else:
						qtag = questag.tag(value)
						sbox = searchGoogle(qtag)
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = sbox, outLen = len(sbox), date = date, uname = uname)
				if cksearch == None and is_state != True and dialogue.test(ques_arr) and whFile.search(dialogue.test(ques_arr)+rmspace):
					dialog = dialogue.test(ques_arr)+" "+value
					print("Dialogue test: "+dialog)

					whfile = whFile.search(dialogue.test(ques_arr)+rmspace)
					qtagAll = questagAll.tag(dialog.lower())
					print("Question tag All: "+qtagAll)
					qtagAll = qtagAll.replace(" ","")
						
					for tag in range(len(whfile)):
						f1con = whfile[tag].rstrip("\n").split("/")
						distance = damerau_levenshtein.damerau(qtagAll,f1con[0].replace(" ",""))
						if distance < mindist:
							mindist = distance
							maxdata = f1con[2]

					print("mindist ques distance: "+str(mindist))
					if mindist <= 10:
						box.append([value])
						box.append([maxdata])
						#print(box)
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
						
							

				if cksearch == None and re.match(r'(.*ဟိုတယ်.*|.*ဟော်တယ်.*|.*တည်းခိုခန်း.*|.*hotel.*|.*မိုတယ်.*|.*motel.*)',value):
							
					if hotelSearch.search(rmspace):
						hotel = hotelSearch.search(rmspace)+"+hotel"
						hbox = searchGoogleHotel.search(hotel,box,value)
						hletter = "hotel"
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = hbox, outLen = len(hbox), date = date, hletter = hletter, uname = uname)					
				if cksearch == None and re.match(r'(.*သွား.*|.*လမ်းညွှန်.*|.*ဘယ်နား*|.*ဝေး.*)',value):
								
					svalue = rmspace.rstrip("။")
					gcheck = "ok"
					gmletter = "အခု "+uname+" မေးတဲ့ မေးခွန်း နှင့် ပတ်သက် ပြီး ကျွန်တော် google map မှာ ဒါ ရှာတွေ့ ပါတယ် ခင်ဗျာ 😀️ အောက်က လင့်ခ်ကို နှိပ်ပြီး လမ်းကြောင်း ကို သိရှိနိုင်ပါတယ် ခင်ဗျာ ..."
					box.append([value])
					box.append([gmletter,svalue,gcheck])
					date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
					return render_template("chatresult.html", out = box, outLen = len(box), date = date, uname = uname)
				if cksearch == None and youtubeSearch.search(rmspace):
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

