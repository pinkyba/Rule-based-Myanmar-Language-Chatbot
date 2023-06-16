#!/usr/bin/python
import sys
import re

myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
ngaThat = r'င်'
aThat = r'်'


#fp = open(f,"r")



def segment(f):
	out = open("tag","w")
	BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
	sb =  BreakPattern.sub("/" + r"\1", f)

	sbs = sb.split("/")
	sbslen = len(sbs)
		
	for m in range(1,sbslen):
		out.write(sbs[m]+" "+"_"+" "+"_"+"\n")
	out.write("\n")

