class Stack:
    def __init__(self):
        self.stkList=[]
    def isEmpty(self):
        return self.stkList==[]
    def length(self):
        return len(self.stkList)
    def push(self,items):
        self.stkList.append(items)
    def pop(self):
        if self.isEmpty():
            print 'stack is empty you can not pop from empty stack'
        else:
            return self.stkList.pop()
    def peek(self):
        return (len(self.stkList)-1)

    
s=Stack()
s.push(5)
print s.pop()
s.pop()    
print s.items
