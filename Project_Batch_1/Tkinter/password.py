# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = str(web_entry.get())
    username = str(user_entry.get())
    password = str(pw_entry.get())
    #Create a list that that saves all three to a csv file.
    with open(file="./txt/file.txt", mode="a") as txt_file:
        txt_file.write(str(f"{website} | {username} | {password}\n"))
        web_entry.delete(0,END)
        pw_entry.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="./png/logo.png")
canvas.create_image(100,100,image=password_logo)
canvas.grid(row=0,column=1)


#Label
web_label = Label(text="Website:")
web_label.grid(row=1,column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2,column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)

#Entries
web_entry = Entry(text="",width=35)
web_entry.grid(row=1,column=1,columnspan=2)

user_entry = Entry(text="",width=35)
user_entry.insert(0, "bilal.m.omar@gmail.com")
user_entry.grid(row=2, column=1,columnspan=2)

pw_entry = Entry(text="", width=20)
pw_entry.grid(row=3,column=1)

#Button

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)




window.mainloop()