##01.iv.   (ii. Flow chart to python code)
total=int(input("enter the total no of people going for the play: "))
min_teach=int(input("enter the minimum no of teachers: "))
max_teach=int(input("enter the maximum no of teachers: "))
teach=min_teach
print()
print("all possible combinations")
print()
print("S  T")
for i in range (min_teach,max_teach+1):
    stu=total-teach
    print(stu,teach)
    teach=teach+1




    
##v. (iii. flow chart to python code)

total=int(input("enter the total no of people going for the play: "))
min_teach=int(input("enter the minimum no of teachers: "))
max_teach=int(input("enter the maximum no of teachers: "))
teach=min_teach
min_cost=total*12 #Highest possible cost if all are adults
for i in range (min_teach,max_teach+1):
    stu=total-teach
    cost=stu*5+teach*12
    if cost<min_cost :
        min_cost=cost
    teach=teach+1
print("minimum cost: ",min_cost)


##Extend

total=int(input("enter the total no of people going for the play: "))
if total<10 :
	print()
     	print("error: total can’t be below 10")
else:
min_teach=total//10
max_teach=total//2
teach=min_teach
print()
print("all possible combinations")
print()
print("S  T")
for i in range (min_teach,max_teach+1):
 stu=total-teach
   	 print(stu,teach)
   	 teach=teach+1


   	 
##02.iv.(ii.- flow chart to python code)

mile=1 # milegue
gas=2 #gas station
rest=3 #rest area
burg=4 #burger area
while (mile%gas!=0)or(mile%rest!=0)or(mile%burg!=0):
    mile=mile+1
print("Closest gas station, rest area, Burger King at the same time: ",mile,"miles")
iii.-flow chat to python code

##Extend

mile=1 # milegue
gas=2 #gas station
rest=3 #rest area
burg=4 #burger area
count=0
dis=int(input("Enter the distance: "))
print("no of coincidence of having gas station, rest area, Burger King all at the same time in",dis,"miles:")
while dis!=mile:
    mile=mile+1
    if (mile%gas==0)and(mile%rest==0)and(mile%burg==0):
        print("at",mile,"th mile")

##03. iii. 
        
fraction=1/2	
strangers=3
rem=1
while strangers!=0:
    rem=(rem+1)/fraction
    strangers = strangers -1
print("initial apple amount: ",int(rem))

##03. iv.

print("Ex: 1/2 , 1/4 , 1/10")
fraction=input("Enter the fraction of apples gave away: ")
frac=int(fraction[2])   #convert fraction input to a integer
person=int(input("Enter the no. of people that gave apples away: "))
rem=int(input("Enter the remainig no. of apple: "))
while person!=0:
    rem=frac*(rem+1)
    person=person-1
print("initial apple amount: ",int(rem))
