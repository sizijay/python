class WaitingLine:

    def __init__(self):
        self.pendingList = []

    def arrival(self,vehicle):
        self.pendingList.append(vehicle)

    def departure(self,licensePlateNumber):
        vehicle = None
        for i in range (0,len(self.pendingList)):
            if(licensePlateNumber==self.pendingList[i][0]):
                vehicle = self.pendingList.pop(i)
                break
        return vehicle

class Garage:
    def __init__(self):
        self.parkingList = []
        self.maximum = 10
        self.occupied = 0

    def arrival(self,vehicle):
        self.parkingList.append(car)        
        self.occupied += 1
        
    def departure(self,licensePlateNumber):
        vehicle = None
        waitingList=[]
        while(not self.parkingList==[]):
            a=self.parkingList.pop(0)
            if a[0]==licensePlateNumber:
                a[1]+=1
                vehicle=a
                break
            else:
                a[1] +=2
                waitingList.append(a)
            
            
        for i in range(0,len(self.parkingList)):
            self.parkingList[i][1] += 1

        while(not waitingList==[]):
            self.parkingList.insert(0,waitingList.pop())

        self.occupied -= 1

        return vehicle


laughfsParking = Garage  ()
pendingList = WaitingLine()
print("........* * * * * * * * * <<<<<< WELCOME TO LAUGHFS PARKING>>>>>> * * * * * * * * *...........")
print("* * * * * * * *instructions:- a<LicensePlate> - Arrival  d<LicensePlate> - Departure  EXIT - Exit * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

while(True):
    print(" ")
    instructions = raw_input("Enter your instructions -> ")
    
    if(instructions=="EXIT"):
        break
    else:
        instructionsType = instructions[0]
        licensePlateNumber = instructions[1:]

        if(instructionsType=="a"):
            isVehicleValid = True
            for i in laughfsParking.parkingList:
                if(i[0]==licensePlateNumber):
                    isVehicleValid = False
                    break
            if(isVehicleValid):
                for i in pendingList.pendingList:
                    if(i[0]==licensePlateNumber):
                        isVehicleValid = False
                        break
            if(isVehicleValid):
                car = [licensePlateNumber,0]
                if (laughfsParking.maximum>laughfsParking.occupied):
                    laughfsParking.arrival(car)
                    print("vehicle "+licensePlateNumber+" added to the laughfs Parking")
                else:
                    pendingList.arrival(car)
                    print("sorry parking is full. vehicle "+licensePlateNumber+" added to the pendingline")
            else:
                print("vehicle exists. Please check the License Plate Number")
                
            
        elif(instructionsType=="d"):
            vehicle = None
            vehicleDetector = 0
            
            for i in laughfsParking.parkingList:
                if(i[0]==licensePlateNumber):
                    vehicleDetector = 1
                    break
            if(vehicleDetector == 0):
                for i in pendingList.pendingList:
                    if(i[0]==licensePlateNumber):
                        vehicleDetector = 2
                        break
                
            if(vehicleDetector == 1):
                vehicle = laughfsParking.departure(licensePlateNumber)
                if(not pendingList.pendingList==[]):
                    pendingVehicle = pendingList.pendingList.pop(0)
                    laughfsParking.arrival(pendingVehicle)
                    print("Room for new vehicle, pending vehicle "+pendingVehicle[0]+" added to laughfs Parking")

            elif(vehicleDetector == 2):                
                vehicle = pendingList.departure(licensePlateNumber)

            else:
                print("vehicle not Found. Please Check the License Plate Number")

            if(not vehicleDetector == 0):
                print("vehicle "+vehicle[0]+" departed. It moved "+str(vehicle[1])+" times")    
                       
                    
        else:
            print("you have given wrong instructions...")
    
        
    
    
            
            
    



