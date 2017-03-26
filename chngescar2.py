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
while not (w[0] == "end"):
    x = input("\nif a car enter input a, space, then the license plate number.\nif a car leaves input d, space, then the license plate number.\nif that's all input end.\n\n>>>")

    w = x.split()
    if(w[0] == "a"):
        if(count1 == 10):
            print("Park is FULL")
            outline.enqueue(w[1])
            
        else:
            print("\ncar",w[1],"parked in the garage\n")
            count1 = count1 + 1
            times.append(w[1])
            q.enqueue(w[1])

    elif(w[0] == 'd'):
        for i in times:
            if (i==w[1]):
                j=q.items.index(w[1])
                h=q.size()
        
                if j==1:
                    if(not q.isEmpty()):
                        while not q.isEmpty():
                            r=q.dequeue()
                            #print ("dequeue")
                    
                            if (r == 'w[1]'):
                                print ("\ncar "+w[1]+" release from car park.\n")
                                h=q.size()
                                for z in range(h):
                                    
                                    if(not q.isEmpty()):
                                        #print("entered")
                                        q1.enqueue(q.dequeue())
                                        z+=1
                                #print (list)
                            elif not (r == 'w[1]'):
                                q2.enqueue(r)
                                #print(q2.items)
                                #continue
                                
                        for z2 in range(q2.size()):
                            if(not q2.isEmpty()):
                                q.enqueue(q2.dequeue())
                                z2+=1
        
                        for z3 in range(q1.size()):
                            while(not q1.isEmpty()):
                                q.enqueue(q1.dequeue())
                            
                                z3+=1
                                #print (q.items)
                                
                elif not j==1:
                    print("\nno vehicle matched\n")
            else:
                print ("\n"+w[1]+" is not in the Garage! Please check the plate number again..\n")
                pass

print (q.items)
print (q1.items)
print (q2.items)
