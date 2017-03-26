class Queue:#Creating the queue class
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

def increment():#When this function is called the number of moves in all vehicles of the queue is increased by 1
        while not garage.isEmpty():
            e=garage.dequeue()
            c=e[len(e)-1]
            e=e[:len(e)-1]+str(int(c)+1)
            garage1.enqueue(e)
        while not garage1.isEmpty():
            e=garage1.dequeue()
            garage.enqueue(e)
            

#creating 3 queue objects
garage=Queue()
waiting=Queue()
garage1=Queue()
#messages for the command line interface
print("==============================Laughs parking garage=============================")
print("\n*************************Instructions****************************")
print("*Enter the state&licence plate number seperated by a white space")
print("*State:   a-for Arrival   d-for Depature")
print("*Licence plate number:  Eg-GP8782")
print("*Enter 'e 0000' to terminate the program")
print("*****************************************************************")

while True:#creates a never ending loop
    if not garage.size()==10:
        if waiting.isEmpty():
            e=raw_input("\nThere is room in the garage,enter state & licence plate number ")
            try:
                x,y=e.split()
                if x=="e" and y=="0000":#when user enters 'e 0000',the program terminates
                    exit()
                if x=="a":#when garage is not full&waiting line is empty,the licence numbers of arriving vehicles are enqueued to the garage queue
                          #with movements(1)
                    found=0
                    for i in garage.items:#checking whether the vehicle is already in the garage
                        if i[:len(i)-1]==y:
                            found=1
                    if found==0:
                        garage.enqueue(y+"1")
                        print("The vehicle "+y+" arrived to the parking garage")
                    else:
                        print("The vehicle "+y+" is already in the garage,please check the licence plate number")
                elif x=="d":#when garage is not full,waiting line is empty& a departure line is read,the program search in the garage queue and removes the relavant vehicle
                    found=0
                    for i in garage.items:
                        if i[:len(i)-1]==y:
                            found=1
                            garage.items.remove(i)
                            increment()#increase the movements of remaining vehicles
                            print("Vehicle has moved "+i[len(i)-1]+" times in the garage")
                    if found==0:
                        print("Sorry the given vehicle is not in our garage,please check the licence plate number")
            except:
                print("There is something wrong in your input,please check the instructions")
                        
        else:  #when the garage is not full& waiting line is not empty the first vehicle in the waiting queue goes into the garage
            r=raw_input("\nThere is room in the garage,the car "+waiting.peek()+" can go into garage,press e to proceed ")
            if r=="e":
                a=waiting.dequeue()
                garage.enqueue(a+"1")
                print("The vehicle "+a+" arrived to the parking garage")

    elif garage.size()==10:#when the garage is full,the licence numbers of arriving vehicles are enqueued to the waiting queue
        e=raw_input("\nThe garage is full now,enter state & licence plate number ")
        try:
            x,y=e.split()
            if x=="e" and y=="0000":
                exit()
            if x=="a": 
                found1=0
                found2=0
                for i in garage.items: #checking whethere the vehicle is already in the garage or waiting queue
                    if i[:len(i)-1]==y:
                        found1=1
                for i in waiting.items:
                    if i[:len(i)]==y:
                        found2=1
                if found1==0 and found2==0:
                    waiting.enqueue(y)
                elif found1==1 and found2==0:
                    print("The vehicle "+y+" is already in the garage")
                elif found1==0 and found2==1:
                    print("The vehicle "+y+" is already in the waiting list")
            elif x=="d":#when departure line is read,the program searches for the vehicle in the garage queue or waiting list&removes it
                found=0
                for i in garage.items:
                    if i[:len(i)-1]==y:
                        found=1
                        garage.items.remove(i)
                        increment()
                        print("Vehicle has moved "+i[len(i)-1]+" times in the garage")    
                if found==0:
                    try:
                        waiting.items.remove(y)
                        print("The vehicle "+y+" has moved 0 times in the garage")
                    except:
                        print("Sorry the given vehicle is not in our garage,please check the licence plate number")#if not found in both garage & waiting list,an exception is generated
        except:
              print("There is something wrong in your input,please check the instructions")#when the input command is incorrect,this exception is generated
                        

            
            
            
                


    

                    
            
                
            
                
            
                
                

