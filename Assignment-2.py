#defining queue class
class queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
#required queues and list      
arrival=queue()
depature=queue()
waiting=[]
print("There are 10 space at the Park" ) #mention the size of the park
#introduse arrival and depature
print("Arrival:-a\nDepature:-d\nExit:-e")
while True:
    #if (arrival.size()<=9):    # fixed the queue size
    waiting=raw_input("Arrival or Depaure or Exite:-") #choose arrival or depature
    
    if waiting=='a':     #if it is arrival mention what to do
        if arrival.size()==10:
            print("'Park is full'\n Wait till your chance")
            continue
        print("Welcome \nYou can park here")
        arrival.enqueue(raw_input("Enter the licen number")) 
        x=(arrival.size())
        y=str(10-x)
        print("There are" +y+ "spaces")
        
    elif (waiting=='d'):    # if it is a depature, mention what to do.
        x=(raw_input("Enter your licen number"))
        while (not arrival.isEmpty()):  #I'm not able to find the error of this part. Try to remove relevant vehicle.   
            k=arrival.dequeue()
            if (k != x):
                depature.enqueue(k)
            else:
                print("Thank you for comming")
        while (not depature.isEmpty()):
            arrival.enqueue(depature.dequeue())
            
    elif waiting=='e':
        print("Thank you")
        exit()
    
    else:      #mention the step that if park is full
        continue

