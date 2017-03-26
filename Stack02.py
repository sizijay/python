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

a=Stack()
b=Stack()
c=Stack()

a.push(4)
a.push(9)
a.push(2)

b.push(3)
b.push(7)
b.push(8)
b.push(4)

y=0
while b.isEmpty()==False and a.isEmpty()==False:
	if a.size()!=0 and b.size()!=0:
		x=a.pop()+b.pop()+y
	elif a.size==0 and b.size()!=0:
		x=b.pop()+y
	elif b.size==0 and a.size != 0:
		x=a.pop()+y
	
	if x<10:
		c.push(x)
		y=0
	
	else:
		c.push(x%10)
		y=1
	if a.size()==0 and b.size()==0:
	    if x<10:
	        c.push(x)
	        y=0
	
	    else:
	        c.push(x%10)
while c.size>0:
	print c.pop(),

