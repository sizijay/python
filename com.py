class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        print (self.items)

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
q=Queue()

while not (w[0] == "end"):
    x = input("""if a car enter input a, space, then the license plate number.
if a car leaves input d, space, then the license plate number.
if that's all input end.\n""")

    w = x.split()
    if(w[0] == "a"):
        if(count1 == 10):
            print("Park is FULL")
            outline.enqueue(int(w[1]))
            
        else:
            print("car",w[1],"parked in the garage")
            count1 = count1 + 1
            times.append(w[1])
            q.enqueue(int(w[1]))

    if(w[0] == 'd'):
        j=q.items.index(int(w[1]))
        h=q.size()
        y=0
        s=Stack()
        q1=Queue()
        q2=Queue()
        list=[]
        if j==1:
            while list==[]:
                r=int(q.dequeue())
                print ("dequeue")
            
                if int(r)==int(w[1]):
                    print ("car "+w[1]+" release from car park.")
                    for z in range(h):
                        if(not q.isEmpty()):
                            q1.enqueue(q.dequeue())
                            z+=1
                    #print (list)
                    for z2 in range(q2.size()-1):
                        if(not q2.isEmpty()):
                            q.enqueue(q2.dequeue())

                            z2+=1
                    for z1 in range(q1.size()-1):
                        if(not q1.isEmpty()):
                            q.enqueue(q1.dequeue())
                    
                            z1+=1
                    #print (q.items)
            
                elif not int(r)==int(w[1]):
                    q2.enqueue(r)
                    print(q2.items)
                    continue
            
         

    #print (q.items)
    #print (outline)    








        
print (q.items)
print (q.items.count(123))

