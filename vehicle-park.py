class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def peek(self):
        return self.items[len(self.items)-1]
    
  

q1=Queue()
q2=Queue()
backup=Queue()
cnt=[]

print("\nThe Laughs parking garage welcomes you!\n Enter a_XXXXXX for arrival.\n Enter d_XXXXXX for departure.\n Enter numq1 to see the current number of vehicles in the garage.\n Enter numq2 to see the current number of vehicles in the waiting list.\n Enter northermost to view the Nothermost vehicle.\n Enter exit to exit\n ")
while True:

    x=input("Enter your command>>>")
   


    
    if x[:2]=="a ":
        p=x[2:len(x)]
        
        if q1.size()<10:
            print("The vehicle with the license plate number "+(str(p))+" has entered to the garage.")
            q1.enqueue(p)
            cnt.append(p)
        else: 
            print("Sorry, there are no spaces in the Parking Garage! Please wait...")
            q2.enqueue(p)

    elif x=="exit":
        
        print("\nThank you for using our sevices.\nPlease visit again!")
        exit()

    
    elif x=="numq1":
        print("The current number of vehicles in the parking garage are "+str(q1.size())+".")

    elif x=="numq2":
        print("The current number of vehicles in the waiting list are "+str(q2.size())+".")

    elif x[:2]=="d ":
        p=x[2:len(x)]
        j=q1.size()
        while (not q1.isEmpty()):
            k=q1.dequeue()
            if (k != p):
                backup.enqueue(k)
            else:
                print("The vehicle with the license plate number "+k+" has departed from the garage.")
                print("Vehicle has moved "+str(cnt.count(k))+" times..")
                while (k in cnt):
                    cnt.remove(k)
        if (j!=backup.size()):
            while (not backup.isEmpty()):
                t=backup.dequeue()
                q1.enqueue(t)
                cnt.append(t)
        else:
            while (not backup.isEmpty()):
                t=backup.dequeue()
                q1.enqueue(t)

        while (not q2.isEmpty()):
            b=q2.dequeue()
            if (b != p):
                backup.enqueue(b)
            else:
                print("The vehicle with the license plate number "+b+" has departed from the garage.")
                print("Vehicle has moved 0 times.. Hasn't even entered the garage..!")
        while (not backup.isEmpty()):
                q2.enqueue(backup.dequeue())

        
        if ((not q2.isEmpty()) and (q1.size()==9)):
            z=q2.dequeue()
            q1.enqueue(z)
            print("\nThe vehicle with the license plate number "+z+" has entered to the garage to fill the empty space..")


    elif (x==""):
        continue
                

        
            

            
        
        
        
                
                
        
        

    
        
        
       
    
        
        
        
    

