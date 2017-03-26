import math
def findDelta(a,b,c):
	delta = b**2 - (4*a*c)
	if delta >= 0:
		return True
	else:
		return False

def findReturns(a,b,c):
	x1 = ((-b) + math.sqrt((b**2)-(4*a*c)))/2*a
	x2 = ((-b) - math.sqrt((b**2)-(4*a*c)))/2*a
	print x1
	print x2





print"The format is ax^x+bx+c"
userInput = raw_input("Enter a expression:")

a = int(userInput[0])
b = int(userInput[5:6])
c = int(userInput[8:])
if findDelta(a,b,c) == True:
	print findReturns(a,b,c)
else:
	print "Theroots are complex"
