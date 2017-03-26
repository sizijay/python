class Stack:
    def __init__(self):
        self.stkList=[]
    def isEmpty(self):
        return self.stkList==[]
    def length(self):
        return len(self.stkList)
    def push(self,items):
        self.stkList.append(items)
    def popItem(self):
        if self.isEmpty():
            print 'stack is empty you can not pop from empty stack'
        else:
            return self.stkList.pop()
    def peek(self):
        return (len(self.stkList)-1)

s=Stack()
def post_fix():
    postfixinput = raw_input("Enter Post Fox Expression: ")
    operand=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    operation=['+','-','*','/']
    for i in postfixinput:
        if i not in operation:
            s.push(i)
        elif i in operation:
            num1=int(s.popItem())
            num2=int(s.popItem())
            if i=='+':
                ans=num2+num1
                s.push(ans)
            elif i=='-':
                ans=num2-num1
                s.push(ans)
            elif i=='*':
                ans=num2*num1
                s.push(ans)
            elif i=='/':
                ans=num2/num1
                s.push(ans)
    return 'Answer: '+str(s.popItem())

print post_fix()
        
