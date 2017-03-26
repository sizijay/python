class Stack:
     def __init__(self):
         self.items =[]

     def isEmpty(self):
         return self.items ==[]

     def push(self,item):
         return self.items.append(item)
       

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def printt(self):
         if self.items==None:
             print("empty")
         else:
            print(self.items)

s=Stack()
s.push(5)
s.printt()

s.pop()
s.push(2)
s.peek()
s.pop()
print(s.size())
s.push(1)
s.pop()
s.push(7)
s.push(6)
s.printt()
