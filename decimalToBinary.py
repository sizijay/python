class Stack:
    def __init__(self):
        self.listStack = []
    def isEmpty(self):
        return self.listStack == []
    def push(self,item):
        self.listStack.append(item)
    def peek(self):
        return (len(self.listStack)-1)
    def size(self):
        return len(self.listStack)
    def pop(self):
        return self.listStack.pop()
    
while True:    
    def divideBy2(decNumber):
        remstack = Stack()

        while decNumber > 0:
            rem = decNumber % 2
            remstack.push(rem)
            decNumber = decNumber // 2

        binString = ""
        while not remstack.isEmpty():
            binString = binString + str(remstack.pop())

        return binString

    print(divideBy2(input('Enter decimal num-:')))
