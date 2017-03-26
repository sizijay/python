# importing tkinter class  for GUI development
from tkinter import *
import tkinter.messagebox


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
        return len(self.qList) == 10

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


# this method is run when OK button is clicked
# get whatever filled in text fields and clears the fields for the next entry
def giveEntry(event):
    # a message is displayed if the text fields are empty when ok button is pressed
    if (enter.get() == "" or ID.get() == ""):
        tkinter.messagebox.showinfo("ERROR", "Fill Both Text Fields Before Submitting!!!")
    # if not this will call another method and clear the text fields
    else:
        change(enter.get().lower(), ID.get())
        enter.delete(0, END)
        ID.delete(0, END)


# manages the order of cars in the queue and displays it on the interface
def listMe():
    id1['text'] = mainQ.itemName(0)
    id2['text'] = mainQ.itemName(1)
    id3['text'] = mainQ.itemName(2)
    id4['text'] = mainQ.itemName(3)
    id5['text'] = mainQ.itemName(4)
    id6['text'] = mainQ.itemName(5)
    id7['text'] = mainQ.itemName(6)
    id8['text'] = mainQ.itemName(7)
    id9['text'] = mainQ.itemName(8)
    id10['text'] = mainQ.itemName(9)
    # calls the inform method to print the current status of the queue
    inform()


# manages the order of cars in the waiting list and displays it on the interface
def waiting():
    id11['text'] = mainQ.itemName(10)
    id12['text'] = mainQ.itemName(11)
    id13['text'] = mainQ.itemName(12)
    id14['text'] = mainQ.itemName(13)
    id15['text'] = mainQ.itemName(14)
    id16['text'] = mainQ.itemName(15)
    id17['text'] = mainQ.itemName(16)
    id18['text'] = mainQ.itemName(17)
    id19['text'] = mainQ.itemName(18)
    id20['text'] = mainQ.itemName(19)
    # calls the inform method to print the current status of the queue
    inform()


# check for the current status of the queue ( full or have space)
def inform():
    l = mainQ.size()
    if (l >= 10):
        status['text'] = "Garage is Full !!!"
    else:
        status['text'] = "You Have Space To Enter A Car ..."

def removed(p):
    for i in ml:
        if(i == p):
            ml.remove(i)

# this method does all the main work of the system
# adding a new car and removing a car from the queue is done by this method
def change(enter, ID):
    if (enter == "a"):
        # if first 10 items are filled in the queue, a message is displayed
        # new car is added to the queue but will be displayed in the waiting list
        if (mainQ.isFull() == True):
            tkinter.messagebox.showinfo("NO SPACE", "Queue is full !!!")
            mainQ.enqueue(ID)
            # calls the waiting method to refresh the order of the waiting order
            waiting()
        else:
            mainQ.enqueue(ID)
            # calls the waiting method to refresh the order of the main queue
            listMe()
            # calls the waiting method to refresh the order of the waiting order
            waiting()
    elif (enter == "d"):
        # whenever you try to dequeue from an empty queue an error message is displayed
        if (mainQ.isEmpty() == True):
            err = "Queue Is Empty... Something Is Wrong In Your Inputs"
            tkinter.messagebox.showinfo("ERROR", err)
        else:
            # call and get the index of the removing item and assign it to a variable
            w = mainQ.index(ID)
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
                removed(p)
                print(ml)
                # displays the message for the number of times that the car has moved inside the garage
                info = "Your Car Has Been Moved " + n + " Times"
                tkinter.messagebox.showinfo("INFO", info)

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
                info = "Your Car Has Been Moved " + n + " Times"
                tkinter.messagebox.showinfo("INFO", info)

                while not (mainQ.isEmpty() == True):
                    r = mainQ.dequeue()
                    nextQ.enqueue(r)

                while not (nextQ.isEmpty() == True):
                    mainQ.enqueue(nextQ.dequeue())

            # calls the waiting method to refresh the order of the main queue
            listMe()
            # calls the waiting method to refresh the order of the waiting order
            waiting()
    else:
        # if the input is neither 'a' nor 'b', it will be an invalid input
        tkinter.messagebox.showinfo("ERROR", "Invalid Input")


# declare a list to keep the moving count of cars inside the parking garage
ml = []
# implementing a main queue to keep the order of the cars that enters to the parking garage
mainQ = Queue()
# this queue is used to fill up when a car in the middle of the main queue is taken out
# so that this helps to keep the order correct
nextQ = Queue()
# makes the main frame of the GUI
root = Tk()
# change the title of the main window
root.wm_title("Laughs Parking Garage ")

# *****entry section*****
# creating labels, text fields and the button
title1 = Label(root, text="Type Input And License Plate Number Here : ", fg="blue")
label1 = Label(root, text="Enter Input (a or d) : ")
label2 = Label(root, text="License Plate : ")
enter = Entry(root)
ID = Entry(root)
ok_button = Button(root, text="OK")

# *****inserting entry section into the grid format*****
title1.grid(columnspan=2, sticky=W)
label1.grid(row=1, sticky=W)
label2.grid(row=2, sticky=W)
enter.grid(row=1, column=1)
ID.grid(row=2, column=1)
ok_button.grid(row=3, column=1, sticky=E, ipadx=60)
# binding a command to the left button click
# when the left button is clicked, it will run the give_entry method
ok_button.bind("<Button-1>", giveEntry)

# ****creating the main car list(labels) inside the parking garage****
title2 = Label(root, text="List Of Cars In The Park : ", fg="blue")
lbl1 = Label(root, text="Vehicle 1")
lbl2 = Label(root, text="Vehicle 2")
lbl3 = Label(root, text="Vehicle 3")
lbl4 = Label(root, text="Vehicle 4")
lbl5 = Label(root, text="Vehicle 5")
lbl6 = Label(root, text="Vehicle 6")
lbl7 = Label(root, text="Vehicle 7")
lbl8 = Label(root, text="Vehicle 8")
lbl9 = Label(root, text="Vehicle 9")
lbl10 = Label(root, text="Vehicle 10")

# ****creating the main car list (car license plate number) inside the parking garage****
id1 = Label(root, text="Empty")
id2 = Label(root, text="Empty")
id3 = Label(root, text="Empty")
id4 = Label(root, text="Empty")
id5 = Label(root, text="Empty")
id6 = Label(root, text="Empty")
id7 = Label(root, text="Empty")
id8 = Label(root, text="Empty")
id9 = Label(root, text="Empty")
id10 = Label(root, text="Empty")

# *****inserting car list into the grid format*****
title2.grid(row=5, columnspan=2, sticky=W)
lbl1.grid(row=6)
lbl2.grid(row=7)
lbl3.grid(row=8)
lbl4.grid(row=9)
lbl5.grid(row=10)
lbl6.grid(row=11)
lbl7.grid(row=12)
lbl8.grid(row=13)
lbl9.grid(row=14)
lbl10.grid(row=15)

id1.grid(row=6, column=1)
id2.grid(row=7, column=1)
id3.grid(row=8, column=1)
id4.grid(row=9, column=1)
id5.grid(row=10, column=1)
id6.grid(row=11, column=1)
id7.grid(row=12, column=1)
id8.grid(row=13, column=1)
id9.grid(row=14, column=1)
id10.grid(row=15, column=1)

# **** creating the waiting list*******
title3 = Label(root, text="Waiting List (upto 10 cars) : ", fg="green")
lbl11 = Label(root, text="Waiting 1")
lbl12 = Label(root, text="Waiting 2")
lbl13 = Label(root, text="Waiting 3")
lbl14 = Label(root, text="Waiting 4")
lbl15 = Label(root, text="Waiting 5")
lbl16 = Label(root, text="Waiting 6")
lbl17 = Label(root, text="Waiting 7")
lbl18 = Label(root, text="Waiting 8")
lbl19 = Label(root, text="Waiting 9")
lbl20 = Label(root, text="Waiting 10")

id11 = Label(root, text="Empty")
id12 = Label(root, text="Empty")
id13 = Label(root, text="Empty")
id14 = Label(root, text="Empty")
id15 = Label(root, text="Empty")
id16 = Label(root, text="Empty")
id17 = Label(root, text="Empty")
id18 = Label(root, text="Empty")
id19 = Label(root, text="Empty")
id20 = Label(root, text="Empty")

# *****inserting waiting list into the grid format*****
title3.grid(row=16, columnspan=2, sticky=W)
lbl11.grid(row=17)
lbl12.grid(row=18)
lbl13.grid(row=19)
lbl14.grid(row=20)
lbl15.grid(row=21)
lbl16.grid(row=22)
lbl17.grid(row=23)
lbl18.grid(row=24)
lbl19.grid(row=25)
lbl20.grid(row=26)

id11.grid(row=17, column=1)
id12.grid(row=18, column=1)
id13.grid(row=19, column=1)
id14.grid(row=20, column=1)
id15.grid(row=21, column=1)
id16.grid(row=22, column=1)
id17.grid(row=23, column=1)
id18.grid(row=24, column=1)
id19.grid(row=25, column=1)
id20.grid(row=26, column=1)

# ***** creating the status bar*******
status = Label(root, text="You Have Space To Enter A Car ...", fg="red", relief=SUNKEN, anchor=W, width=37)
status.grid(row=4, columnspan=3, sticky=W, )

# the following methods will run when executing the program
listMe()
waiting()
inform()

# to keep the main frame displayed
root.mainloop()
