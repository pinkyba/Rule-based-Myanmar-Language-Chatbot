import sys

data1 = sys.argv[1] 	# original data line by line (uniq data)
data2 = sys.argv[2] 	# pos tagged data line by line

f1 = open(data1,"r")
f2 = open(data2,"r")


f1line = f1.readlines()
f2line = f2.readlines()


tmp1 = ""
for i in range(len(f1line)):
	tmpArr = []
	ch = 0
	tmp1 = f1line[i].rstrip("\n")
	for j in range(len(f2line)):
		fcon = f2line[j].rstrip("\n").split("/")
		if tmp1 == fcon[0]:
			tmpArr.append(fcon[0]+"/"+fcon[1])
			ch =1
			
	for k in range(len(tmpArr)):
		print(tmpArr[k])
	if ch == 0:
		print(tmp1)
