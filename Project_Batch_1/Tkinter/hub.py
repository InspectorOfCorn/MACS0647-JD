from tkinter import *

window = Tk()
window.title("My first gui program")
window.minsize(width = 500, height = 300)
window.config(padx=20,pady=20)
#Label

my_label = Label(text="I am a label", font=("Cambria",24,"bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "Russia"
#Another way to edit text via function

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Enter", command=button_clicked)
button.grid(column=2,row=1)

new_button = Button(text="This changes it too", command=button_clicked)
new_button.grid(column=3,row=0)
#Entry Component
input = Entry(width=10)
input.grid(column=4,row=3)




window.mainloop()