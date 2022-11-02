# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip
from random import choice, randint, shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_entry = pw_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save():
    
    website = str(web_entry.get())
    username = str(user_entry.get())
    password = str(pw_entry.get())
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {username}\nPassword: {password}")
        
        if is_ok:
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

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3, column=2)




window.mainloop()