class cars():
    def __init__(self,number):
        self.item = number
        self.moves=0

    def start(self):
        self.moves = self.moves+1
    def licenseno(self):
        return self.item
    def movement(self):
        return self.moves+1

class queue():
    def __init__(self):
        self._qlist=list()
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self._qlist)
    def enqueue(self,item):
        self._qlist.append(item)
    def dequeue(self):
        assert not self.isEmpty()
        return self._qlist.pop(0)
q=queue()
w=queue()
p=[]
while True:
    a=raw_input("next vehicle")
    car=cars(a[2:])
    if a == "show":
        print q._qlist
        print w._qlist
    if a[:1]=="a":
        if len(q)>=10:
            print("Sorry,not enough space")
            w.enqueue(a[2:])
        else:
            print("Welcome,now you can enter")
            q.enqueue(a[2:])
    elif a[:1]=="d":
        if  a[2:] in q._qlist:
            while not len(q)==0:
                f=q.dequeue()
                f.start()
                if f==a[2:]:
                    print("Good Bye."+ str(f.movement())+"has moved")
               
                else:
                    p.append(f)
                    f.start()
                    
            while len(p) != 0:
                q.enqueue(p.pop(0))
                continue
            while not len(w)==0:
                while len(q)<10:
                    print(" sorry for the delay, now u can enter")
                    g=w.dequeue()
                    q.enqueue(g)
        else:
            print("This car is not in the park")
    else:
        print("invalid number")
