#queue class
class Queue():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, value):
        self.items.append(value)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

#vehicle class
class Vehicle():
    def __init__(self, _lplate):
        self.item = _lplate         #there are 2 attributes here
        self.moves = 0              #one to store license no. and one to store moves amount
        
    def start(self):
        self.moves = self.moves + 1 #no of moves is increased by one when this method is called
    def license_no(self):
        return self.item            #license no is returned in this method
    def movements(self):
        return self.moves + 1       #no of total moves is returned when this method is called





#from Queue_class import Queue
#from Vehicle2 import Vehicle
    
#needed queues
garage = Queue()   
removal = Queue()  
waiting = []       

#instructions to be printed
print("For Arrival   : a license_no \nFor Departure : d license_no \nExit ") 
                                                                             
while True:
    inpln = raw_input("\n>>> :")
    inpln = inpln.lower()        

    #extra code to show the vehicles in garage and waiting queue
    if inpln == "show":
        sh = garage.size()
        print ("Vehicles in Garage")
        for f in range (0, sh):            
            print garage.items[f].license_no(), garage.items[f].moves
        print ("Vehicles in Waiting queue")
        for g in waiting:
            print g.license_no()
    
    #when a license no is the input         
    elif inpln[:2] == "a " and inpln[2] != " ":                                 
        print "\nWelcome!"                                                        
        car = Vehicle(inpln[2:])
        state = True

        #since we cant have 2 cars with same license no. we check whther this car is already there in the garage 
        for i in garage.items:
            if car.item == i.item:
                print "Vehicle already in Garage\nPlease recheck License No."
                state = False
                break
            else:
                pass

        #we check in waiting   
        for i in waiting:
            if car.item == i.item:
                print "Vehicle already in Waiting queue\nPlease recheck License No."
                state = False
                break
            else:
                pass

        #if car not already there we enqueue if there is space    
        if state == True:
            if garage.size() == 10:                             
                print "Garage is full!! \nPlease wait in line "
                waiting.append(car)
                
            #else put in waitng queue
            else:                                               
                print "You can enter the parking garage!"       
                garage.enqueue(car)                             
                                                                
    #when d license no is the input
    elif inpln[:2] == "d " and inpln[2] != " ":             
        print "\nThanks for coming!"                          
        length = garage.size()
        state1 = False
        state2 = False

        #check whether vehicle in garage 
        for i in garage.items:
            if i.license_no() == inpln[2:]:
                state1 = True
                break
            else:
                pass
        #if not in garage check whether in queue   
        if state1 == False:
            for i in waiting:
                if i.license_no() == inpln[2:]:
                    state2 = True
                    break
                else:
                    pass
        #if in garage remove car through this method    
        if state1 == True:
            while garage.size() != 0:
                y = garage.dequeue()
                if (y.license_no() != inpln[2:]):
                    y.start()
                    removal.enqueue(y)
                else:                                                  
                    print (y.license_no() + " has moved " + str(y.movements()) + " times in the garage")
            while not removal.size() == 0:
                garage.enqueue(removal.dequeue())
        
        #if in waiting queue remove car through this method
        elif state2 == True:
            for i in waiting:
                if i.license_no() == inpln[2:]:
                   print (i.license_no() + " has moved 0 times in the garage")
                   waiting.remove(i)
                   
        #if car not available in both queues
        else:
            print("Wrong License plate no. Please recheck!!")
        
        #if a car departs, enqueue one car to the garage    
        if garage.size() < 10:                              
            if waiting != []:                               
                print "There is a space for one vehicle!"   
                wcar = waiting.pop(0)
                garage.enqueue(wcar)
    
    #if input is invalid
    else:
        print "Invalid input"
