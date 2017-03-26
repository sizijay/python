"""#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

zero=float(0)
pos=float(0)
neg=float(0)

for i in arr:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1

print("{0:.6f}".format(pos/n))
print("{0:.6f}".format(neg/n))
print("{0:.6f}".format(zero/n))"""

"""#!/bin/python

import sys


n = int(raw_input().strip())
x=n-1
m=1
while (x>=0):
    print(" "*x+"#"*m)
    x-=1
    m+=1"""


"""#!/bin/python

import sys


time = raw_input().strip()
ap=time[8:]
timex=time[:8].split(":")
if(ap.lower()=="pm"):
    if timex[0]!="12":
        timex[0]=str(int(timex[0])+12)
else:
    if timex[0]=="12":
        timex[0]="00"

print(timex[0]+":"+timex[1]+":"+timex[2])"""
    































