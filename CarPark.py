class WaitingLine:

    def __init__(self):
        self.waitingList = []

    def arrival(self,car):
        self.waitingList.append(car)

    def departure(self,licensePlateNumber):
        car = None
        for i in range (0,len(self.waitingList)):
            if(licensePlateNumber==self.waitingList[i][0]):
                car = self.waitingList.pop(i)
                break
        return car

class Garage:
    def __init__(self):
        self.parkingList = []
        self.max = 10
        self.used = 0

    def arrival(self,car):
        self.parkingList.append(car)        
        self.used += 1
        
    def departure(self,licensePlateNumber):
        car = None
        waitingList2=[]
        while(not self.parkingList==[]):
            x=self.parkingList.pop(0)
            if x[0]==licensePlateNumber:
                x[1]+=1
                car=x
                break
            else:
                x[1] +=2
                waitingList2.append(x)
            
            
        for i in range(0,len(self.parkingList)):
            self.parkingList[i][1] += 1

        while(not waitingList2==[]):
            self.parkingList.insert(0,waitingList2.pop())

        self.used -= 1

        return car


CarPark = Garage()
waitingLine = WaitingLine()
print("* * * * * * * * * * * * * * * * * * * * * * * * WELCOME TO CAR PARK * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * *commands:- a<LicensePlate> - Arrival  d<LicensePlate> - Departure  EXIT - Exit * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

while(True):
    print(" ")
    command = raw_input("Enter Command -> ")
    
    if(command=="EXIT"):
        break
    else:
        commandType = command[0]
        licensePlateNumber = command[1:]

        if(commandType=="a"):
            isCarValid = True
            for i in CarPark.parkingList:
                if(i[0]==licensePlateNumber):
                    isCarValid = False
                    break
            if(isCarValid):
                for i in waitingLine.waitingList:
                    if(i[0]==licensePlateNumber):
                        isCarValid = False
                        break
            if(isCarValid):
                car = [licensePlateNumber,0]
                if (CarPark.max>CarPark.used):
                    CarPark.arrival(car)
                    print("Car "+licensePlateNumber+" added to the Carpark")
                else:
                    waitingLine.arrival(car)
                    print("No room for car in car park. Car "+licensePlateNumber+"added to the Waitline")
            else:
                print("Car already found. Please check the License Plate Number")
                
            
        elif(commandType=="d"):
            Car = None
            carfinder = 0
            
            for i in CarPark.parkingList:
                if(i[0]==licensePlateNumber):
                    carfinder = 1
                    break
            if(carfinder == 0):
                for i in waitingLine.waitingList:
                    if(i[0]==licensePlateNumber):
                        carfinder = 2
                        break
                
            if(carfinder == 1):
                Car = CarPark.departure(licensePlateNumber)
                if(not waitingLine.waitingList==[]):
                    waitcar = waitingLine.waitingList.pop(0)
                    CarPark.arrival(waitcar)
                    print("Room for new car, Waited car "+waitcar[0]+" added to Carpark")

            elif(carfinder == 2):                
                Car = waitingLine.departure(licensePlateNumber)

            else:
                print("Car not Found. Please Check the License Plate Number")

            if(not carfinder == 0):
                print("Car "+Car[0]+" departed. It moved "+str(Car[1])+" times")    
                       
                    
        else:
            print("Wrong Command")
    
        
    
    
            
            
    



