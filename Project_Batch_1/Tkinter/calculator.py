#11R30

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1 - n2

def subtract(n1,n2):
    return n1 - n2

def add(n1,n2):
    return n1 + n2


#-------------------Ui Setup-----------------------#

from tkinter import *

window = Tk()
window.config(padx=20, pady=20,width=200,height=200)
window.title("Calculator")

#Label
output = Label(text="--------------",width=35)
output.grid(row=0, column=1)

#Buttons
button_0 = Button(text="0", width=5,)
button_0.grid(row=5,column=1,)
button_0.config(padx=3,pady=3,)

button_1 = Button(text="1", width=10,)
button_1.grid(row=1,column=0)

button_2 = Button(text="2", width=10)
button_2.grid(row=1, column=1)

button_3 = Button(text="3", width=10)
button_3.grid(row=1,column=2)

button_4 = Button(text="4", width=10)
button_4.grid(row=2,column=0)

button_5 = Button(text="5", width=10)
button_5.grid(row=2,column=1)

button_6 = Button(text="6", width=10)
button_6.grid(row=2,column=2)

button_7 = Button(text="7", width=10)
button_7.grid(row=3, column=0)

button_8 = Button(text="8", width=10)
button_8.grid(row=3, column=1)

button_9 = Button(text="9", width=10)
button_9.grid(row=3,column=2,)

button_add = Button(text="+", width=10)
button_add.grid(row=1, column=4)

button_multiply = Button(text="*", width=10)
button_multiply.grid(row=2, column=4)
button_multiply.config(highlightthickness=0)
button_division = Button(text="/", width=10)
button_division.grid(row=3,column=4)

button_subtraction = Button(text="-", width=10)
button_subtraction.grid(row=4,column=4)

button_sum = Button(text="=", width=10)
button_sum.grid(row=5,column=4)






window.mainloop()

