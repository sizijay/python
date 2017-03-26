class Queue:
    def __init__(self):
        self.items=[]
    def clear(self):
        self.items=[]
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

arrivals=Queue()
departures=Queue()
back=Queue()
wait=[]

print "Welcome to the garage...\nPlease enter your license plate number:\n for arrivals, please enter:a license number\n for departures, please enter:d license number\n if you want to depart, type 'exit'\n"
print "To view the current number of vehicles in the garage, type 'garage'"
print "To view the current number of vehicles waiting to enter the garage, type 'wait'"
print "To view the frontmost vehicle, type 'frontmost vehicle'"
while True:
    number=raw_input("Enter:")

    if (number=="exit"):
        print ("You may exit!")
        exit()


#arriving of vehicles to the garage and printing whether the garage is full or not and arrival message        
    elif (number.lower()[:2]=="a "):
        if(arrivals.size()>=10):
            print("\nFull...!Please wait\n")
            z=number[2:len(number)]
            wait.insert(0,z)
        else:
            print("\nWelcome!")
            arrivals.enqueue(number[2:len(number)]+"1")
            print("vehicle number %s arrived" % number[2:len(number)])


#departing of vehicles from the garage and printing departing messages
     
    elif (number.lower()[:2]=="d "):
        j=0
        l=arrivals.size()
        while (not arrivals.isEmpty()):
            x=arrivals.dequeue()
            if(number[2:len(number)]!=x[:len(x)-1]):
               departures.enqueue(x[:len(x)-1]+str(int(x[len(x)-1:])+1)) 
               back.enqueue(x)
            else:
                print("Vehicle number %s departed" % x[:len(x)-1])
                print ("This has moved %s times in the garage" % x[len(x)-1])


#checking the vehicle in the waiting list
        for i in wait:
            if (i==number[2:len(number)]):
                print ("Vehicle %s can now enter the garage" % wait.pop(wait.index(i)))
                print ("Vehicle didn't move inside the garage")
                j=1
                                   
                
        
#checking whether a vehicle with given license plate number is present in the garage
        if (departures.size()==l and j==0):
            print("This vehicle %s is not in the garage" % number[2:len(number)])
            while (not back.isEmpty()):
                  arrivals.enqueue(back.dequeue())
            departures.clear()
            continue
#moving back vehicles after giving space to a vehicle in the queue
        while (not departures.isEmpty()):
                arrivals.enqueue(departures.dequeue())
        back.clear()
        continue

#room available message
        if (wait!=[] and arrivals.size()<10):
            print("Now you can enter the garage")
            p=1
            while (p==1):
              w=raw_input("There is an empty space in the garage.Want to give access to enter?(yes/no) )")                     
              if (w.lower()=="yes"):                     
                  n=wait.pop()
                  print("welcome to the garage!")
                  arrivals.enqueue(n+"1")
                  print("Vehicle number %s arrived to the garage" % n)
                  p=2
              elif (w.lower()=="no"):
                  p=2
              else:
                   print ("please enter 'yes' or 'no'")
                   pass
#checking the number of vehicles in the queue
    elif (number.lower()=="garage"):
             print("There are %s vehicles in the garage" % str(arrivals.size()))
#checking the number of vehicles in the waiting list
    elif (number.lower()=="wait"):
             print("There are %s vehicles in the waiting list" % str(len(wait)))
#view the northernmost vehicle
    elif (number.lower()=="frontmost vehicle"):
        if(arrivals.isEmpty!= True):
             print("The frontmost vehicle number is %s" % arrivals.peek()[:len(arrivals.peek())-1])
        else:
             print("There are no vehicles in the garage")

#checking for wrong input commands
    elif(number==""):
         continue
    else:
         print("Make sure you enter the correct command, Thank you!")                            
                                     
                                    
                                     
                                     
                                   
