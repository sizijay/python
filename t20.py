def projected(rate,overs):
    oleft=20-overs
    pscore=(oleft*rate)
    return (pscore)

def currentTotal(rate,overs):
    ctotal=(rate*overs)
    return (ctotal)

def projectedTotal(pscore,ctotal):
    ptotal=(pscore+ctotal)
    return (ptotal)

overs,rate=int(input("\nEnter the number of overs played... ")),int(input("Enter the current run rate... "))

i=0
print ("\n\t\t----Projected Scores----\n")
while (i<4):
    ratex=((rate//1)+i)
    if (i==0):
        print ("\t* Current RR\t"+str(projectedTotal(projected(rate,overs),currentTotal(rate,overs))))
    else:
        print ("\t* "+str(ratex)+" per over\t\t"+str(projectedTotal(projected(ratex,overs),currentTotal(rate,overs))))
    i+=1
    
    
    
