class Queue():
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,items):
        self.items.insert(0,items)
    def dequeue(self):
        self.items.pop()                       
        
Q=Queue()
W=Queue()
A=input("If it is an arrivel enter 'a'\nIf it is a depature enter 'd'\n>>>")
CPN=str(input("Please enter your car plate number :"))

if (A=="a"):
    if (Q.size()<10):
        print("you have a space room ")
        Q.enqueue(CPN)
    else:
        print("Dear customer thanks for waiting. Now you have a free space ")
        Q.enqueue(W.dequeue())
else:
    print("Sorry! You don't have a room and you have to wait for it.!")
    W.enqueue(CPN)

#elif (A=="d"):
    
