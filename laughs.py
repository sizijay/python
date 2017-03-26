class Queue():
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()

Q=Queue()    
A=input("If it is an arrivel please enter \"a\", if it is a depature please enter \"d\" ")
if (A=="a"):
    if (Q.size()<10):
        print("You have a room ")
        CN=input("Enter your car number :")
        Q.enqueue(CN)
    else:
        print("Sorry you don't have a room ")

            
      
    
    
