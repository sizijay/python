import random
def genarateRandom():
	return random.randint(1,4)

def checkWinLoose(user,computer):
	if(user == "r" and computer == 3):
		return "you : Rock , Computer : Scissor You Win !!"
	elif(user == "s" and computer == 1):
		return "you : Scissor , Computer : Rock You Loose!!"
	elif(user == "s" and computer == 2):
		return "you : Scissor , Computer : Paper You Win !!"
	elif(user == "paper" and computer == 3):
		return "you : paper , Computer : Scissor You loose !!"
	elif(user == "p" and computer == 1):
		return "you : paper , Computer : Rock You Win !!"
	elif(user == "r" and computer == 2 ):
		return "you : Rock , Computer : paper You Loose !!"
	else:
		return "Game Tied Try Again :-P"



print "r - Rock\np - Paper\ns - Scissor"
while True:
	x = raw_input("please Enter a r or s or p:(-1 to quit):")
	if x == "-1":
		print "You are quited"
	else:
		print checkWinLoose(x,genarateRandom())

