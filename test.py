print("Ex: 1/2 , 1/4 , 1/10")
fraction=input("Enter the fraction of apples gave away: ")
frac=int(fraction[2])   #convert fraction input to a integer
person=int(input("Enter the no. of people that gave apples away: "))
rem=int(input("Enter the remainig no. of apple: "))
while person!=0:
    rem=frac*(rem+1)
    person=person-1
print("initial apple amount: ",int(rem))
