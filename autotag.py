#grep -v '[/]' ./postag-all

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

f1 = open(file1,"r") 		# file for postagging
f2 = open(file2,"r")		# pos tagged file

f1line = f1.readlines()
f2line = f2.readlines()

for i in range(len(f1line)):
	tmp = ""
	out = ""
	tmp1 = ["null"]
	ck = 0

	f1con = f1line[i].rstrip("\n").split(" ")
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
	#print(tmp1)
	#print(ch)
	out = tmp+"/"+f1line[i].rstrip("\n")
	print(out)


f1.close()
f2.close()
