class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items==[]
        
s=Stack()
t=Stack()
print("Type QUIT to exit")
while (True):
    word=input(">>>")
    word=word.upper()
    l=word[:3]
    if word[:5]=="ENTER":
        s.push(word[6:len(word)])
    elif len(word)==3:
        if s.size==1:
            print("Please enter two operands first in order to do calculations")
            continue
        else:
            y=float(s.pop())
            x=float(s.pop())
            if l=="ADD":
                t.push(x+y)
            elif l=="SUB":
                t.push(x-y)
            elif l=="MUL":
                t.push(x*y)
            elif l=="DIV":
                t.push(x/y)
            elif l=="POW":
                t.push(x**y)
            elif l=="CLR":
                s=Stack()
        
    elif word[:4]=="QUIT":
        break
    elif word[:7]=="CLRLAST":
        s.pop()
    elif word[:6]=="RESULT":
        print("Answer is "+str(t.pop()))
    else:
        print("Please enter a valid command")
        continue
    
#print("*****Sisira Creations*****")
            
            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
                                
        
        
            
            
        
        
        
        
        
        
        
        
        
        
