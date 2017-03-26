def average(s1,s2,s3):
    avg=((s1+s2+s3)/3)
    if (avg>=60):
        if (avg<70):
            print ("\nYour Average is "+str(avg)+"%. You have passed with a MARGINAL average...\n")
        else:
            print("\nYour Average is "+str(avg)+"%. You have passed with a good average. Congratulations!\n\n\t\t***************************************\n")
    else:
        print("\nYour average is "+str(avg)+"%. You have Failed! \n")

while True:
    name=input("\nEnter your Name...  ")
    print("\nHello " +name+"! Enter your marks for the 3 subjects........\n")
    s1=int(input("Subject 1 = "))
    s2=int(input("Subject 2 = "))
    s3=int(input("Subject 3 = "))

    if ((s1>100) or (s2>100) or (s3>100) or (s1<0) or (s2<0) or (s3<0)):
        print("\nPlease enter valid marks...\n")
        continue
    else:
        print("\n\t\t---"+name+"'s Results---\n")
        average(s1,s2,s3)
    x=input("Enter 'x' if you want to terminnate the programme.. OR press enter to check another....\n")
    if (x=="x"):
        exit()
    else:
        continue
