import tkinter.messagebox
from tkinter import *
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    pas.delete(0, 'end')
    up = ''
    lo = ''
    sym = ''
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    symbol = ['!', '@', '#', '$', '%', '(', '+']
    for i in range(4):
        up += choice(upper)
        lo += choice(lower)
        sym += choice(symbol)
    j = [i for i in up + lo + sym]
    shuffle(j)
    k = ''.join(j)
    pas.insert(0, k)
    pyperclip.copy(k)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(web.get()) == 0 or len(user.get()) < 1 or len(pas.get()) < 1:
        tkinter.messagebox.showinfo(title=f'Error', message=f'Empty Slot!!!')

    else:
        ques = tkinter.messagebox.askokcancel(title=web.get(), message=f'These are the details entered:\n '
                                                                       f'\nEmail:{user.get()}\n\nPassword: {pas.get()}')
        if ques:
            with open('password.txt', mode='a') as f:
                f.write(f'Website: {web.get()}  |UserName:  {user.get()}  |Password:  {pas.get()}\n')
            web.delete(0, 'end')
            user.delete(0, 'end')
            pas.delete(0, 'end')
            web.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=10, pady=10)

canvas = Canvas(height=500, width=500)
img = PhotoImage(file='logo.png')
canvas.create_image(250, 150, image=img)
canvas.pack()

web = Entry(width=50)
web.place(x=150, y=290)
web.focus()

answer = Label(text='Website:', font='Georgia, 10')
answer.place(x=85, y=290)

user = Entry(width=50)
user.place(x=150, y=330)

email = Label(text='Email/UserName:', font='Georgia, 10')
email.place(x=40, y=330)

pas = Entry(width=25)
pas.place(x=150, y=370)

password = Label(text='Password:', font='Georgia, 10')
password.place(x=80, y=370)

gen_pass = Button(text='Generate Password', width=18, command=pass_generator)
gen_pass.place(x=320, y=370)

final = Button(text='Add', width=42, command=save)
final.place(x=150, y=410)
window.mainloop()