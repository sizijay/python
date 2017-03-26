class Garage:
    def __init__(self):
        self.garageList=[]
        self.max=10
        self.usage=0
        self.garageList2=[]
    def arriveCar(self,car):
        
            self.garageList.insert(0,car)
            self.usage +=1
            
    def departure(self,licensePlateNumber):
        
        #x = None
        waitingList2=[]
        while(not self.garageList==[]):
            x=self.garageList.pop()
            if licensePlateNumber==car[0]:
               #x[1]+=1
               #waitingList2.append(x)
               pass
               #return car
               
               #break
            else:
               x[1]+=1
               
               waitingList2.insert(0,x)
               #break
            
        
                
        """for i in range(0,len(self.garageList)):
            self.garageList[i][1] += 1"""

        while(not waitingList2==[]):
            self.garageList.insert(0,waitingList2.pop())
            

        self.usage -= 1
        print x[0],
        print "gone"
        print waitingList2 
        print self.garageList
        print x[1],
        print "times move"
        return car
       

        #return x

class WaitingLine():
    def __init__(self):
        self.waitingList=[]

    def inputting(self,car):
        self.waitingList.append(car)
        print("carpark is full n we arrove it pending list")
    def output(self,licensePlateNumber):
        
        for i in range (0,len(self.waitingList)):
            if(licensePlateNumber==self.waitingList[i][0]):
                car = self.waitingList.pop(i)
                print("*******")
                break
        return car

CarPark=Garage()
WaitingList=WaitingLine()

while True:
    command= raw_input("Enter Your Command>: ")
    commandLine=command[0]
    licensePlateNumber=command[1:]
    car=[licensePlateNumber,1]
    
    if (commandLine =="a"):
        if CarPark.usage<CarPark.max:
           CarPark.arriveCar(car)
           print car[0],
           print "car on the garage"

        else: 
            WaitingList.inputting(car)
            print car[0],
            print "no room for arrive your car.therefor plz waiting in waiting list for a few minutes"

    

    elif(commandLine =="d"):
        for i in CarPark.garageList:
            if i[0]==licensePlateNumber:
               CarPark.departure(licensePlateNumber)
               #print car[0],
               #print"is depature now.wel come.come again"
            else:
                pass
               
              
               
               



               
        for x in WaitingList.waitingList:
            if x[0]==licensePlateNumber:
               WaitingList.output(licensePlateNumber)
               print [0],
               print "is depature in waitinglist."
               
                

