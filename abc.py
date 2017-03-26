class stack:
    def _init_(self):
        self.items=[]
        def isEmpty (self):
            return self.items==[]
        def pop (self):
            return self.items.pop()
        def peek (self):
            return self.items[len (self.items())-1]
        def size (self):
            return len(self.items)

        s= stack()
        s.push(20)
        print (s.items)
        x=12
        print (x)
