class Block:
    def __init__(self, pid, start, size):
        self.startAddr = start
        self.size = size
        self.isFree = False
        self.pid = pid
        self.next = None

    def endAddr(self):
        return self.startAddr + self.size

    def makeFree(self):
        self.isFree = True
        self.pid = "Free"

    def setPID(self, pid):
        self.pid = pid
        self.isFree = False

class Memory:
    def __init__(self, size):
        self.head = Block("Free", 0, size)
        self.head.makeFree()

    def isExists(self, pid):
        cur = self.head
        while cur!=None:
            if cur.pid == pid:
                return True
            cur = cur.next
        return False

    def allocate(self, pid, size):
        if self.isExists(pid):
            print("processId" + pid + " is already exists")
            return
        
        cur = self.head
        prev = None
        found = False
        while cur != None and not found:
            if cur.isFree and (size <= cur.size):
                found = True
            else:
                prev = cur
                cur = cur.next

        if found:
            if cur.size == size:
                cur.setPID(pid)
            else:
                b = Block(pid, cur.startAddr, size)
                if prev != None:
                    prev.next = b
                else:
                    self.head = b
                b.next = cur
                cur.size -= size
                cur.startAddr += size
            print("Allocated!")
            
        else:
            print("No space")

    def terminate(self, pid):
        cur = self.head
        while cur!=None:
            
            if cur.pid == pid:
                cur.makeFree()
                self.merge()
                print("process {0} terminated!".format(pid))
                return
          
            cur = cur.next
            
    def merge(self):    
        cur = self.head
        while cur.next.next!=None:
            if cur.pid == "Free" and cur.next.pid == "Free":
                cur.size = cur.size+cur.next.size                    
                cur.next= cur.next.next
          
            
            cur = cur.next
        if cur.next.next==None:
                if cur.pid == "Free" and cur.next.pid == "Free":
                   cur.size = cur.size+cur.next.size                    
                   cur.next= None
        
        
            
    def show(self):
        print('')
        cur = self.head
        while cur != None:
            print("pid:{0}\trange:{1}-{2}\tsize:{3}".format(cur.pid, cur.startAddr, cur.endAddr(), cur.size))
            cur = cur.next
        
x=("\n\n\n*************************Memory Management************************\nFor the Allocation ................................................................................................\n\t\tEnter : 'A'\n\nFor the Termination................................................................................................\n\t\tEnter : 'T'\n\n\t\tEnter : 'RAM' to view the current Allocations\n\n\t\tEnter : 'EXIT' to Terminate the Programme\n\n\n\n")
for i in x:
    print (i),

size = raw_input("Enter the Memory Size :>>>")
os_size = raw_input("Enter the OS Size :>>>")

memory = Memory(int(size))
memory.allocate("OS", int(os_size))


	
while True:
    inp = raw_input(">>>")
    if (inp==""):
        continue
    if inp.upper() == "A":
        pid=raw_input("\nEnter the Process ID..........\n\t\t>>>")
        size=int(raw_input("\nEnter the size.........(K)\n\t\t>>>"))
        memory.allocate(pid,size)

    elif inp.upper() == "T":
        pid=raw_input("\nEnter the Process ID..........\n\t\t>>>")
        memory.terminate(pid)

    elif inp.upper()== "RAM":
        memory.show()

    elif (inp.upper() == "exit"):
        exit()
    
