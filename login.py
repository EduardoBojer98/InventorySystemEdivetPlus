from tkinter import *
from tkinter import messagebox
import operations

root = Tk()
root.title('Inventory System EdivetPlus Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='image/login.png')
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


#######################------------------username----------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=107)

######################--------------------password------------------
def on_enterP(e):
    password.delete(0, 'end')

def on_leaveP(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Pin')

password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Pin')
password.bind('<FocusIn>', on_enterP)
password.bind('<FocusOut>', on_leaveP)

Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=177)
######################--------------------------------------------------------

Button(frame, width=39, pady=7, text='Sing In', bg='#57a1f8', fg='white', border=0,command=operations.signin(user,password)).place(x=35, y=204)

label = Label(frame, text="dont have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sing_up = Button(frame, width=6, text="Sing up", border=0, bg='white', cursor='hand2', fg='#57a1f8')
sing_up.place(x=215, y=270)

root.mainloop()
