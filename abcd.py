class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def select(self,item):
        return self.items.count(item)

    def display(self):
        print (self.items)

out = []
outline = Queue()
times = []
count1 = 0
n = 0
w = [""]
x = ""
y=0
list=[]
q=Queue()
q1=Queue()
q2=Queue()

print ("""                      ~~~Welcome to LAUGHS CAR PARK~~~""")


while not (w[0] == "end"):
    x = input("""\n>>If a car enter input a, space, then the license plate number.
>>if a car leaves input d, space, then the license plate number.
>>if that's all input end.\n""")

    if(x == ""):
        print ("Try again with a valid input")

    else:    
    
        w = x.split()
        if(w[0] == "a"):
            if(count1 == 10):
                print("Park is FULL")
                print ("Vehicle parked in Outline.")
                outline.enqueue(w[1])
            
            else:
                print("Car",w[1],"parked in the garage")
                count1 = count1 + 1
            
                q.enqueue(w[1])

        elif(w[0] == "d"):
        
            h1=q.size()
        
            if w[1] in q.items:

                    while not q.isEmpty():
                    
                        r=q.dequeue()
                    
                        if (r == w[1]):
                        
                            times.append(w[1])
                            print ("car "+w[1]+" released.")
                            print("number of times car moved",times.count(w[1]))
                            print ("Thank you !")
                            count1=count1 - 1
                            h1=q.size()
                        
                            for z in (0, q.size()):
                                if(not q.isEmpty()):
                                    h = q.dequeue()
                                    times.append(h)
                                    q1.enqueue(h)
                                
                    
                        else:
                            times.append(r)
                            q2.enqueue(r)
                        
                        
                        
                    for z2 in range(q2.size()):
                        if(not q2.isEmpty()):
                            q.enqueue(q2.dequeue())
                        

                    for z3 in range(q1.size()):
                        while(not q1.isEmpty()):
                            q.enqueue(q1.dequeue())
                    
                    if (outline.isEmpty() == False):
                        #while True:
                            if not q.size()== 10:   
                                if(count1 == 10):
                                    print ("Car Park was Filled")
            
                                else:
                                    veh = outline.dequeue()
                                    print("Car",veh,"parked in the garage")
                                    count1 = count1 + 1
            
                                    q.enqueue(veh)
                            else:
                                print ("Car Park is FULL")
                    else:
                        print ("No more vehicles in outline")
                        
            else:
                print("Invalid Input")

        else:
            if(w[0] == "end"):
                print ("\nVehicles currently in Park :")
                print (q.items)

                print ("Vehicles currently in outline : ")
                print (outline.items)

                print ("\nThank you for visiting LAUGHS CAR PARK")
                print ("Have a nice day!!")
            else:
                print("Invalid Input")



