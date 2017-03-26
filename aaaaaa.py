l=["Mango", "Banana", "Apple", "Papaya"]
print (l)
l.pop(3)
print(l)
l.append("Guava")
print(l)
l.insert(2,"papaya")
print(l)
len(l)
print(len(l))
l.pop()
print(l)
l.pop(3)
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print("\n")

stack1=[]
def push(stack_id,e):
    stack_id.append(e)
def pop(stack_id):
    return stack_id.pop()
print(stack1)
push(stack1,"3")
push(stack1,"20")
push(stack1,"50")
push(stack1,"10")
push(stack1,"40")
push(stack1,"10")
print(stack1)
stack1.append("80")
print(stack1)
pop(stack1)
print(stack1)
pop(stack1)
pop(stack1)
print(stack1)
print("\n")

from collections import deque
queue-deque([])
print(queue)





