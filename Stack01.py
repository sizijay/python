class Stack:
    def __init__ (self):
    	self.items=[]
    def peek(self):
    	return self.items[len(self.items)-1]
    def isEmpty(self):
   	return self.items==[]
    def pop(self):
    	return self.items.pop()
    def size(self):
    	return len(self.items)
    def push(self,item):
        self.items.append(item)


s=Stack()

print(s.isEmpty())
s.push(4)
s.push("dog")
print(s.size())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
s.pop()
s.pop()
print(s.size())

