
from tkinter import *
root = Tk()
root.title("evaluator")
app = Frame(root)
app.grid()


label = Label(app, text = "enter expression", fg = "black", bg ="yellow")
label.grid(column = 0 , row = 0, columnspan = 2 , sticky = W)

password = Entry ()
password.grid (column =1  , row = 1 , sticky =W)

button =Button (app, text ="evaluate")
button. grid (column = 0 , row = 3 , sticky = W)
root.mainloop()
