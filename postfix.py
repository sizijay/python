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

def postf(expr):
    for item in expression:
        if (item in operands):
            s.push(item)
        elif (item in operators):
            y=float(s.pop())
            x=float(s.pop())
            if item=="+":
                s.push(x+y)
            elif item=="-":
                s.push(x-y)
            elif item=="/":
                s.push(x/y)
            elif item=="*":
                s.push(x*y)
            elif item=="^":
                s.push(x**y)
        else:
            pass
       


operands=["0","1","2","3","4","5","6","7","8","9"]
operators=["+","-","/","*","^"]
s=Stack()

expression=input("Enter the postfix Expression....")
postf(expression)
print("The answer for the postfix "+expression+" = "+str(s.pop()))
#print ("*****Sisira Creations*****")
