# Implementation of queue class
class Queue:
    def __init__(self):
        self.qList = []

    def dequeue(self):
        return self.qList.pop(0)

    def enqueue(self, item):
        self.qList.append(item)

    def isEmpty(self):
        return len(self.qList) == 0

    def isFull(self):
        return len(self.qList) >= 10

    # returns the index of a particular item in the queue
    def index(self, item):
        return self.qList.index(item)

    # returns the item name of an item in the queue when the index is provided
    def itemName(self, ind):
        if (ind < len(self.qList)):
            return self.qList[ind]
        else:
            return "Empty"  # returns empty if the queue is not filled upto called index

    def size(self):
        return len(self.qList)


# manages the order of cars in the main queue and displays it on the interface
def mainList():
    print("\n ****Main Queue List Of Cars**** \n")
    count = mainQ.size()
    x = 0
    if(count >0):
        while not(x == 10):
            print("Car ", x + 1, " : ",mainQ.itemName(x))
            x += 1
        print("\n")
    else:
        print("-- Nothing In The Parking Garage -- \n")


# manages the order of cars in the waiting list and displays it on the interface
def waitingList():
    count = mainQ.size()
    x = 10
    if(count > 10):
        print("*****Waiting List of Cars**** \n")
        while not(x == count):
            print("Waiting Car ", x - 9, " : ",mainQ.itemName(x))
            x += 1
        print("\n")

# check for the current status of the queue ( full or have space)
def inform():
    l = mainQ.size()
    if (l >= 10):
        print("-- Garage is Full !!! -- \n")
    else:
        print("\n-- You Have Space To Enter A Car -- \n")

# removes the car id from the counting list
def removed(p):
    for i in ml:
        if(i == p):
            ml.remove(i)

# this method does all the main work of the system
# adding a new car and removing a car from the queue is done by this method
def mainFunction(enter, ID):
    if (enter == "a"):
        # if first 10 items are filled in the queue, a message is displayed
        # new car is added to the queue but will be displayed in the waiting list
        if (mainQ.isFull() == True):
            print("\n -- Garage is Full !!! -- \n -- This car will be remain in the waiting list -- \n")
            mainQ.enqueue(ID)
        else:
            mainQ.enqueue(ID)
            print("-- The Car ",ID," Has Been Entered Into The Garage --")
            # calls the inform method to to check the current status of the main queue
            inform()
    elif (enter == "d"):
        # whenever you try to dequeue from an empty queue an error message is displayed
        if (mainQ.isEmpty() == True):
            print("-- Queue Is Empty -- Something Is Wrong In Your Inputs --")
        else:
            # call and get the index of the removing item and assign it to a variable
            w = 0
            try:
                w = mainQ.index(ID)
            except:
                print("-- Invalid Input -- No Such Car Present --")
                return
            # declare a variable to go through the index starting from 0
            a = 0
            # declare a variable to keep the number of times a car moved inside the garage
            n = 0
            if (w < 10):
                # if the removing car is in the main queue
                # all the cars in front of the removing car will be enqueued into the 'nextQ' queue
                while not (a == w):
                    r = mainQ.dequeue()
                    nextQ.enqueue(r)
                    a += 1
                    # all the moving cars license plate number will be added to a list
                    ml.append(r)

                # removing car will bre dequeued form the mainQ
                p = mainQ.dequeue()
                # since we need to count the moving times along with the removal
                # license plate number will be added to the list again
                ml.append(p)
                # get the moved count of the removing car
                n = str(ml.count(p))
                # remove all occurences of removinf car in counting list
                removed(p)
                # displays the message for the number of times that the car has moved inside the garage
                print("-- The Car ",ID," Has Been Diparted From The Garage --")
                print("-- This Car Has Been Moved ",n," Times --")

                # the rest of the cars that are located after the car are also enqueued in the 'nextQ' queue
                while not (mainQ.isEmpty() == True):
                    r = mainQ.dequeue()
                    nextQ.enqueue(r)
                    # also their license plate number will be added to the counting list
                    ml.append(r)

                # all the cars in the 'nextQ' will be again enqueued to the 'main-q' queue
                while not (nextQ.isEmpty() == True):
                    mainQ.enqueue(nextQ.dequeue())
            # if the removing car is from the waiting list
            else:
                # all the cars in front and back will be enqueued to the 'nextQ' queue
                # then again enqueued into the mainQ again
                while not (a == w):
                    r = mainQ.dequeue()
                    nextQ.enqueue(r)
                    a += 1

                p = mainQ.dequeue()
                # since the removal is from the waiting list, the number of times moved should be 0
                n = "0"
                print("-- Your Car Has Been Moved ",n," Times --")

                while not (mainQ.isEmpty() == True):
                    r = mainQ.dequeue()
                    nextQ.enqueue(r)

                while not (nextQ.isEmpty() == True):
                    mainQ.enqueue(nextQ.dequeue())

            # calls the inform method to to check the current status of the main queue
            inform()
    else:
        # if the input is neither 'a' nor 'b', it will be an invalid input
        print("-- Invalid Input --")


# declare a list to keep the moving count of cars inside the parking garage
ml = []
# implementing a main queue to keep the order of the cars that enters to the parking garage
mainQ = Queue()
# this queue is used to fill up when a car in the middle of the main queue is taken out
# so that this helps to keep the order correct
nextQ = Queue()

#display
print("###############################################################")
print("#################### Laughs Parking Garage ####################")
print("###############################################################")
print("<<< Instructions To Proceed >>>")
print("  ~ Enter 'a' or 'd' With The 'License Plate Number' Of The Car.")
print("  ~ Example : a XX-1234")
print("  ~ Type 'check' To Check The List Of Cars Present.")
print("  ~ Type 'exit' To Close The Program. \n") 
inform()
# making a variable named 'enter' for the loop's condition to be true for the first time
enter = ""
#takes a list of inputs until 'exit' is entered by the user
while not(enter.lower() == "exit"):
    enter = input("Enter The Input : ")
    if(enter.lower() == "check"):
        mainList()
        waitingList()
    elif(enter.lower() == "exit"):
        # exit from the program
        exit()
    else:
        # breaking the input into 2 parts from the space
        entry = enter.split(" ")
        # this will ignore the inputs having more than 1 spaces
        if(len(entry) == 2):
            # the 2 parts after spliting are saved to 2 variables 
            form = entry[0].lower()
            plate = entry[1]
            mainFunction(form,plate)
        else:
            print("-- Invalid Input --")



