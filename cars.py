#implementing the class Queue
class Queue:
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

    def view(self):
        t=1
        for i in range (0,len(self.items))[::-1]:
            print ("\t"+str(t)+")   "+self.items[i][:len(self.items[i])-1])
            t += 1
           
            
    def size(self):
        return len(self.items)

#creating two queues
cars=Queue()
back=Queue()
bakc=Queue()
wait=[]

#printing the welcome message and directions to input commands
q="\nWelcome to the Laughs Parking Garage!\n                                     --Enter-- \nFor Arrival    >>>   a license_plate_number   \nFor Departure   >>>   d license_plate_number  \nTo see the current number of vehicles in the garage    >>>    n\nTo see the current number of vehicles in the waiting list   >>>   m\nTo view the Northernmost Vehicle   >>>   north\nTo view current Vehicles   >>>   view\nTo exit the Programme   >>>   exit \n\n              ***** Sizi Creations 2016 *****\n\n\n"
for i in q:
    print (i),
#creating a loop for continuous inputs 
while True:
    inp=raw_input(">>>")
	
    #exit command	
    if (inp=="exit"):
        print ("Thank you for visiting Laughs Car Park!\nCome again & Have a Nice Day!")
        exit()

    #to view the vehicles in the garage & waiting list
    elif (inp.lower()=="view"):
        if (cars.isEmpty()==False):
            print ("\n---Current vehicles in the Garage---\n")
            cars.view()
        else:
            print ("\nNo vehicles in the Garage at the moment\n")
        if (len(wait) > 0):
                print ("\n---Current vehicles in the waiting area---\n")
                x=1
                for j in wait[::-1]:
                    print ("\t"+str(x)+")   "+j)
        else:
            print ("\nNo vehicles in the waiting area at the moment..\n")
	
    #arriving of vehicles to the garage and printing whether the garage is full or not & arriving message
    elif (inp.lower()[:2]=="a "):		
        if (cars.size()>=10):
            print("\nThe Parking Garage is Full! Please wait..\n")
            z=inp[2:len(inp)]
            wait.insert(0,z)
        else:
            print("\nWelcome to the Parking Garage!")
            cars.enqueue(inp[2:len(inp)]+"1")
            print("Vehicle with License plate No."+inp[2:len(inp)]+" has been arrived to the Parking Garage..\n")

    #departing of vehicles from the garage and printing departing messages
    elif (inp.lower()[:2]=="d "):
        j=0
        l=cars.size()
        while (not cars.isEmpty()):
            x=cars.dequeue()
            if (inp.lower()[2:len(inp)]!=x.lower()[:len(x)-1]):
                back.enqueue(x[:len(x)-1]+str(int(x[len(x)-1:])+1))
                bakc.enqueue(x)
            else:
                print("\nVehicle with License plate No."+x[:len(x)-1]+" has been daparted from the Parking Garage..")
                print("Vehicle has moved "+x[len(x)-1:]+" times while in the queue!\n")

        #checking the vehicle in waiting list
        for i in wait:
            if (i.lower()==inp.lower()[2:len(inp)]):
                print("\nVehicle with License plate No."+wait.pop(wait.index(i))+" has been daparted from the waiting area..")
                print("Vehicle hasn't even entered the Garage! (moved times = 0)\n")
                j=1
                
        #checking whether a vehicle with given license plate number is present in the garage
        if (back.size()==l and j==0):
            print("\nNO vehicle for License plate number "+inp[2:len(inp)]+" present in the Parking Garage or waiting area.Please check your License plate number again!\n ")
            while (not bakc.isEmpty()):
                cars.enqueue(bakc.dequeue())
            back.clear()
            continue

        #moving back vehicles after giving space to a vehicle in the queue
        while (not back.isEmpty()):
            cars.enqueue(back.dequeue())
        bakc.clear()
		
        #room available message
        if (wait != [] and cars.size()<10 ):
            print("\nThanks for waiting!\nNow you can enter the Parking Garage..\n")
            p=1
            while (p==1):
                w=raw_input("Do you want next waiting list vehicle to enter the Garage from the waiting area?? (y/n)_")
                if (w.lower()=="y"):
                    n=wait.pop()
                    print("\nWelcome to the Parking Garage!")
                    cars.enqueue(n+"1")
                    print("Vehicle with License plate No."+n+" has been arrived to the Parking Garage..")
                    p=2
                elif(w.lower()=="n"):
                    p=2
                else:
                    print ("\nPlease input 'y' or 'n'....")
                    pass
            print ("\n")                

    #checking the number of vehicles in the queue 
    elif (inp.lower()=="n"):
        print ("\nAt the moment, there are "+str(cars.size())+" vehicle(s) in the garage!\n")

    #checking the number of vehicles in the waiting list
    elif (inp.lower()=="m"):
        print ("\nAt the moment, there are "+str(len(wait))+" vehicle(s) in the waiting list!\n")
    
    #view the northernmost vehicle
    elif (inp.lower()=="north"):
        if (cars.isEmpty()==True):
            print ("\nThere are no vehicles in the Garage or waiting area at the moment!\n")
        elif (cars.isEmpty() == False):
            print ("\nThe northernmost vehicle's License plate number is "+cars.peek()[:len(cars.peek())-1]+"\n")
        

    #checking for wrong input commands	
    elif (inp==""):
        continue
    else:
        print("\nPlease enter the data/command in the correct format.\neg-: a WI0684\n")
		
		
		

