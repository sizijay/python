class queue:
    def __init__(self):
        self.items = []
        
    def clear(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
   
arrived=queue()
extra=queue()
waiting=queue()
waitb=queue()
print("********LAUGH PARK***********")


print("enter:if it is arrival,input a license nmber. if it is departure,input d license number.\n enter e for exit")

while True:
    x=str(input(">>>>"))
    x=x.lower()
    if len(x)>2:
        command=x[:2]
        xx=x[2:]

    if x=='show':
        print(arrived.items)
        print(waiting.items)

    elif x=="e":
        print("Come Again..!")
        break

    elif x=="":
        continue

    elif len(x)<3:
        print("enter a valid command..")
        continue

    elif command=='a ':
        print("Welcome to the laugh park.Vehicle with the license number " + str(xx) + " has arrived to the park.")
        if arrived.size()<10:
            arrived.enqueue(xx)
        
        else:
            print("Sry,park is full.There is no room to park.So plz wait till u gain a room.")
            waiting.enqueue(xx)

    elif command=='d ':
        #print("The vehicle with the license number " + str(x) + " is going to depart from the garage.")

        if xx  not in arrived.items:
            if xx  not in  waiting.items:
                print("The vehicle with the license number " + str(xx) + " is not in the parking")


        while not arrived.size()==0:
            j=arrived.dequeue()
            if j==xx:
                print("The vehicle with the license number " + str(xx) + " departed from the garage.")
            else:
                extra.enqueue(j)
            
        
        while not extra.size()==0:
            arrived.enqueue(extra.dequeue())


##        count=0    
##        move=arrived.dequeue()
##        count=count+1

 
            

        if xx in waiting.items:
            print("The vehicle " + str(xx) + " waited for a room in the garage departed from the parking.The number of times it moved within the garage=0.")
            while (not waiting.isEmpty()):
                r=waiting.dequeue()
                if r!=xx:
                    waitb.enqueue(r)
                else:
                    pass
            while (not waitb.isEmpty()):
                waiting.enqueue(waitb.dequeue())
                
    else:
        continue

       


##      if  x in waiting.items:
##            print("the vehicle with the license number"+ str(x) + "is going to exit.Number of moves done by the vehicle is =0.")
##
##        if x in arrived.items:
##                
##          
##            while not extra.isEmpty():
##                extra.dequeue(x)
##                arrived.enqueue(x)

        if arrived.size()<10 and waiting.size()>10:
            print("There is an empty room available in the park.")
           
            arrived.enqueue(waiting.dequeue())
        
        



