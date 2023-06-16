
f2 = open("tag-all","r")
f2line = f2.readlines()

def tag(qtag):
	tmp = ""
	tmp1 = ["null"]
	ck = 0

	f1con = qtag.split(" ")
	for j in range(len(f1con)):
		ch = 1
		for t in range(len(tmp1)):
			if tmp1[t] == f1con[j]:
				ch = 0
				break
		for k in range(len(f2line)):
			f2con = f2line[k].rstrip("\n").split("/")

			if ch == 1 and f1con[j] == f2con[0] and f2con[1] == "n":
							
				if ck == 1:
					tmp += " "+f2con[0]
					tmp1.append(f2con[0])
					break
				else:
					tmp += f2con[0]
					tmp1.append(f2con[0])
					ck = 1
					break
	return(tmp)

f2.close()
