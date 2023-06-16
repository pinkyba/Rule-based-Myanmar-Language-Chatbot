import sys
import re

f1 = sys.argv[1]
f2 = sys.argv[2]
file1=open(f1,"r")

file2=open(f2,"w")
con=file1.read()

res = re.sub(r'[၊။()&?*+/\…/\’""\'“”–``/\-,./\:]',' ',con)
file2.write(res)
