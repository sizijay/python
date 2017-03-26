class Ram(object):
    def __init__(self, capacity):
        self.head = AllocUnit(-1, 0, capacity)
        self.head.setFree()

    def isExist(self,pid):
        current=self.head
        while (current != None):
            if (current.pid == pid):
                return True
            current=current.next
        return False

    def allocate(self,pid,size):
        if (self.isExist(pid)):
            print ("\nThe process "+pid+" is already running and "+str(size)+"K is allocated to the programme..\n")
            return

        current=self.head
        Availability,previous=0,0
        
        
        while ((current != None) and (Availability==0)):
            if ((current.isFree==True) and (current.size >= size)):
                if (current.size==size):
                    self.setPid(pid)
                else:
                    new=AllocUnit(pid,currrent.lower,size)
                    if (previous != 0):
                        previous.next=new
                    else:
                        self.head=new
                    new.next=current
                    current.size -= size
                    current.lower += size
                    print("\n"+size+"K has successfully been allocated to the process "+pid+"..........\n")
                    Availability=1
            else:
                previous=current
                current=current.next
        if (Availability==0):
            print ("\nNo enough free space for the allocation of "+str(size)+"K...\n")
                        
    def terminate(self,pid):
        current=self.head
        while (current != None):
            if (current.pid == pid):
                current.setFree()
                print("\nProcess with the ID "+pid+" has successfully been Terminated...\n")
            current=current.next

    def viewRam(self):
        print("\tProcessID\t\tRange(K)\t\tAllocatedMemory(K)")
        current=self.head
        while (current != None):
            print("\t"+pid+"\t\t"+str(current.lower)+"---"+current.upper+"\t\t"+str(size))
            current=current.next

class AllocUnit:
    def ___init__(self,pid,lower,size):
        self.size=size
        self.pid=pid
        self.next=None
        self.isFree=False
        self.lower=lower
        self.upper=(lower+size)

    def setFree(self):
        self.isFree=True
        self.pid=-1

    def setPid(self,pid):
        self.pid=pid
        self.isFree=False            


x=("*************************Random Access Memory*************************\nFor the Allocation ................................................................................................\n\t\tEnter : 'A'\n\nFor the Termination................................................................................................\n\t\tEnter : 'T'\n\n\t\tEnter : 'RAM' to view the current Allocations\n\n\t\tEnter : 'EXIT' to Terminate the Programme\n")
"""for i in x:
    print (i),"""

#capacity=int(raw_input("\nEnter the capacity for the RAM......\n"))
R = Ram(2560)

while True:
    inp = raw_input(">>>")
    if (inp==""):
        continue
    if (inp.upper()=="A"):
        pid=raw_input("\nEnter the Process ID..........\n\t\t")
        size=int(raw_input("\nEnter the size.........(K)\n\t\t"))
        R.allocate(pid,size)
    elif (inp.upper()=="T"):
        pid=raw_input("\nEnter the Process ID..........\n\t\t")
        R.terminate(pid)
    elif (inp.upper()=="RAM"):
        R.viewRam()
    elif (inp.upper() == "exit"):
        exit()


















    
