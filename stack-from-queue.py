class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []
        self.p=Queue()
        self.q=Queue()

    def push(self, item):
        self.p.enqueue(item)

    def pop(self):
        while(self.p.size()>1):
            self.q.enqueue(self.p.dequeue())
        deq = self.p.dequeue()
        while(not self.q.isEmpty()):
            self.p.enqueue(self.q.dequeue())
        return deq

s=Stack()
s.push("a")
s.push("b")
s.push("c")
s.push("d")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
