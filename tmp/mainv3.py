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

box = []
greet = [".*hello.*",".*hi.*",".*hey.*",".*ဟယ်လို.*",".*ဟဲလို.*",".*ဟလို.*","ဟိုင်း","ဟေး",".*မင်္ဂလာ.*ပါ.*"]
thank = [".*thankyou.*",".*thanks.*",".*thank.*",".*ကျေးဇူး.*"]
bye = ['.*bye.*','.*goodbye.*','.*seeyou.*','.*ဘိုင့်.*','.*ဘိုင်.*']
greet_res1 = ['မင်္ဂလာ နံနက်ခင်းလေး ပါ ခင်ဗျာ 😁️','မင်္ဂလာ နေ့လည်ခင်းလေး ပါ ခင်ဗျာ 🤗️','မင်္ဂလာ ညနေခင်းလေး ပါ ခင်ဗျာ 😊️','မင်္ဂလာ ညချမ်းလေး ပါ ခင်ဗျာ 🤗️']
greet_res = ['ဘာ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 😊️',
      'လူကြီးမင်း ၏ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ အကူအညီ လိုအပ် ပါ သလဲ ခင်ဗျာ 😀️',
      'လူကြီးမင်း ၏ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ များ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 😊️',
      'လူကြီးမင်း ၏ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး အကူအညီ လိုအပ် နေ ပါ သလား 😀️',
      'လူကြီးမင်း ၏ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး ဘာ များ သိချင် ပါ သလဲ 😊️',
      'လူကြီးမင်း ၏ အလည်အပတ် ခရီး နဲ့ ပတ်သက် ပြီး အကြံဉာဏ် လိုအပ် နေ ပါ သလား 🤔️',
      'ဘာ များ ကူညီ ပေး ရ မလဲ ခင်ဗျာ 🤗️' ]
thank_res = ['ရပါတယ် ဗျာ ....✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ကျေးဇူးတင် ပါ တယ် 🤗️','ဟုတ်ကဲ့ ။ ကျေးဇူးတင် ပါ တယ် ဗျ 😍️','ရပါတယ် ဗျာ .... ✌️ အခု လို ကူညီ ခွင့် ရ တာ ကို ပဲ ဝမ်းသာ ပါ တယ် 😍️','ရပါတယ် ခင်ဗျ 🤗️ ပျော်ရွှင် သော နေ့လေး တစ်နေ့ ဖြစ်ပါစေ ....']
bye_res = ['Bye Bye ❤️','နှုတ်ဆက်ပါတယ် ခင်ဗျာ 🙂️','ဘိုင့်ဘိုင် 😍️','Good Bye 😍️']
bye_res1 = ['ပျော်ရွှင်ဖွယ်ကောင်းသော နေ့လေးတစ်နေ့ ဖြစ်ပါစေ ခင်ဗျာ ✌️','အခု လို လာရောက် မေးမြန်း တဲ့ အတွက် ကျေးဇူးတင်ပါတယ် 🤗️','တစ်နေ့တာ ပျော်ရွှင်ဖွယ်ရာ နေ့လေး ဖြစ် ပါစေ ❤️ ❤️','ကျွန်တော် အကြံပေးတာတွေ က လူကြီးမင်း အတွက် အထောက်အကူ ဖြစ်မယ် လို့ မျှော်လင့် ပါတယ် ခင်ဗျ 😀️']

@app.route('/')
def chatbot():
	return render_template('chatbot.html')

@app.route('/chatbot',methods = ['POST', 'GET'])
def chatresult():
	now = datetime.now()
	dist = 0
	maxdist = 0
	ck = 0

	if request.method == 'GET':
		return render_template("chatresult.html")
	if request.method == 'POST':

		d= datetime.today()
		if d.hour >= 0 and d.hour < 12:
			gres1 = greet_res1[0]
		elif d.hour >= 12 and d.hour < 16:
			gres1 = greet_res1[1]
		elif d.hour >= 16 and d.hour < 19:
			gres1 = greet_res1[2]
		else:
			gres1 = greet_res1[3]

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
			print("greeting check: "+grcheck)
			if grcheck == "g":
				gres = random.choice(greet_res)
				box.append([value])
				box.append([gres1,gres])
				date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
				return render_template("chatresult.html", out = box, outLen = len(box), date = date)
			elif grcheck == "t":
				gres = random.choice(thank_res)
				box.append([value])
				box.append([gres])
				date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
				return render_template("chatresult.html", out = box, outLen = len(box), date = date)
			elif grcheck == "b":
				gres = random.choice(bye_res)
				gres1 = random.choice(bye_res1)
				box.append([value])
				box.append([gres,gres1])
				date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
				return render_template("chatresult.html", out = box, outLen = len(box), date = date)
			elif greetingCheck.greetCheck(value):
				
				gc = greetingCheck.greetCheck(value)
				print("Greeting Check: "+gc)
				box.append([value])
				box.append([gc])
				date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
				return render_template("chatresult.html", out = box, outLen = len(box), date = date)
			else:

				ques = array.city(rmspace)
				if ques == None:
					ques = "no"
				print(ques)
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
				    r''+ques+'.*အဝေးပြေး.*',
				    r''+ques+'.*ထင်ရှား.*နေရာ.*',
				    r''+ques+'.*အထင်ကရ.*နေရာ.*',
				    r''+ques+'.*ဈေးချို.*',
				    r''+ques+'.*ဈေးသက်.*',
				    r''+ques+'.*ဈေးနည်း.*',
				    r''+ques+'.*မြို့မဈေး.*',
				    r''+ques+'.*ဈေး.*',
				    r''+ques+'.*ဆွမ်းဆန်စိမ်း.*',
				    r''+ques+'.*ဆွမ်းကြီးလောင်း.*',
				    r''+ques+'.*တန်ဆောင်တိုင်.*',
				    r''+ques+'.*သင်္ကြန်.*'
				    r''+ques+'.*သွား.*တယ်.*',
				    r''+ques+'.*အနီး\s*တဝိုက်.*',
				    r''+ques+'.*တစ်ဆင့်.*', 
				    r''+ques+'.*သွား\s*မယ်*',
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
				    r''+ques+'.*ဘာဘုရား.*',
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
				    r''+ques+'.*ဘုရား.*',
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
						
						return render_template("chatresult.html", out = box, outLen = len(box), date = date)
						ck = 1
				if ck == 0:
					dictData = retrieveDict.dictionary(rmspace)
					#print(dictData)
					if dictData != None:
						box.append([value])
						box.append([dictData])
						#print(box)
						date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
						return render_template("chatresult.html", out = box, outLen = len(box), date = date)
					else:
	###### Need segmentation ############
						def searchGoogle(svalue):
							title = ""
							des = ""
							link = ""
							isdown = 1
							sdata = searchtag.tag(svalue)
							print("sdata"+sdata)
							if sdata:
								search = sdata
								print("Google Search: "+search)
							else:
								search = svalue

							data = test.scrap(search)
							#print(data)
							static = '/home/pinky/chatbot-test/static/img/'
							files = os.listdir(static)
							for f in files:
								if f == search:
									isdown = 0
							if isdown == 1:
								img = downImg.image(search)
								
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
							path = 'static/img/'+search+'/' 
							files = os.listdir(path)
							img = random.choice(files)
							image = search+'/'+img
							letter = svalue+" နှင့် ပတ်သက် ပြီး ကျွန်တော် google မှာ ဒါ ရှာတွေ့ ပါ တယ် ခင်ဗျာ 😃️ 😀️"
							box.append([svalue])
							box.append([title,des,link,image,letter])
							#print(box)
							return box

						cksearch = questag.tag(value)
						print("Check search tag: "+cksearch)
						cks = cksearch.split("_")
						if len(cks) > 1:

							qtagAll = questagAll.tag(value)
							print("Question tag All: "+qtagAll)
						
							qtmp = qtagAll.split("_")
							#print(qtmp)

							tag = '/home/pinky/chatbot-test/database/postag-ques'
							tagFile = open(tag,"r")
							all_ans = open("ans-all","r")
							ansline = all_ans.readlines()
							tagline = tagFile.readlines()
							for tag in range(len(tagline)):
								f1con = tagline[tag].rstrip("\n").split("|")
								f1tmp = f1con[0].split("_")
									
								dist = 0
								for qt in range(len(qtmp)):
									for ft in range(len(f1tmp)):
										distance = damerau_levenshtein.damerau(qtmp[qt],f1tmp[ft])
										#print("distance"+str(distance))
										if distance == 0:
											dist += 1
											break
								if dist > maxdist:
									maxdist = dist
									maxdata = ansline[tag]
								
							#print("maxdata"+maxdata)
							print("maxdist ques: "+str(maxdist))
							if maxdist >= 5:
								box.append([value])
								box.append([maxdata])
									#print(box)
								date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
								return render_template("chatresult.html", out = box, outLen = len(box), date = date)
							else:
								maxdist = 0
								qtag = questag.tag(value)
								print("Question tag: "+qtag)
							
								qtmp1 = qtag.split("_")
								#print(qtmp)

								tag1 = '/home/pinky/chatbot-test/database/postag-ans'
								tagFile = open(tag1,"r")
								tagline = tagFile.readlines()
								for tag in range(len(tagline)):
									f1con = tagline[tag].rstrip("\n").split("|")
									f1tmp = f1con[0].split("_")
										
									dist = 0
									for qt in range(len(qtmp1)):
										for ft in range(len(f1tmp)):
											distance = damerau_levenshtein.damerau(qtmp1[qt],f1tmp[ft])
											#print("distance"+str(distance))
											if distance == 0:
												dist += 1
												break
									if dist > maxdist:
										maxdist = dist
										maxdata = f1con[1]
								print("maxdist ans: "+str(maxdist))
								if maxdist >= 4:
									box.append([value])
									box.append([maxdata])
									#print(box)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = box, outLen = len(box), date = date)	
								else:
									sbox = searchGoogle(value)
									date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
									return render_template("chatresult.html", out = sbox, outLen = len(sbox), date = date)
						else:
							cbox = searchGoogle(value)
							date = now.strftime("%d/%m/%Y  %I:%M:%S %p")
							return render_template("chatresult.html", out = cbox, outLen = len(cbox), date = date)

if __name__ == '__main__':
	app.run()

