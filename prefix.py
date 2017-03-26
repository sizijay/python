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

def pref(expr):
    for item in expression[::-1]:
        if (item in operands):
            s.push(item)
        elif (item in operators):
            x=float(s.pop())
            y=float(s.pop())
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

expression=input("Enter the prefix Expression....")
pref(expression)
print("The answer for the prefix "+expression+" = "+str(s.pop()))
#print ("*****Sisira Creations*****")
