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
        return self.stkList.pop()
    def peek(self):
        return (len(self.stkList)-1)

class chek_balance_peran:
    stak=Stack()
    boole=True
    
    def chek(self,itemList):
        i=0
        #do below things until i<len of itemList
        while i<+len(itemList):
            #if i='(' push it to the stack
            if itemList[i]=='(':
                self.stak.push('(')
            #chek i=')'
            elif itemList[i]==')':
                #if stack is already empty,so bool=False
                if self.stak.isEmpty()==True:
                    self.boole=False
                #if stack is not empty,then pop()
                elif self.stak.isEmpty()==False:
                    self.stak.pop()
            i+=1
        #if bool=false,stack is allready empty.so  this is not a balance parenthesis.
        if self.boole == False:
            print 'not a balance perantheces'
        #bool=True,stack is empty,this is a balance perantheces.
        elif self.stak.isEmpty()==True:
            print 'blance perantheces'
        else:
            print 'not a balance perantheces'

objct = chek_balance_peran()
while True:
    objct.chek(itemList=list(raw_input('Enter -:')))
