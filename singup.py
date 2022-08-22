from tkinter import *
from tkinter import messagebox
import operations

window= Tk()
window.title("Inventory System EdivetPlus Singup")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

img = PhotoImage(file='image/singup.png')
Label(window, image=img, bg="white").place(x=50, y=50)

frame = Frame(window, width=350, height=370, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text="Sign up", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

################   Pin
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
##################### Pin

def on_enterP(e):
    password.delete(0, 'end')


def on_leaveP(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Pin')


password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Username')
password.bind('<FocusIn>', on_enterP)
password.bind('<FocusOut>', on_leaveP)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

############################ Reepete Pin
def on_enterPR(e):
    passwordR.delete(0, 'end')


def on_leavePR(e):
    name = passwordR.get()
    if name == '':
        passwordR.insert(0, 'Username')


passwordR = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
passwordR.place(x=30, y=220)
passwordR.insert(0, 'Pin repete')
passwordR.bind('<FocusIn>', on_enterPR)
passwordR.bind('<FocusOut>', on_leavePR)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


##############   sign up button

Button(frame,width=39,pady=7,text="Sing Up",bg='#57a1f8',fg='white',border=0,command=operations.signup).place(x=35,y=280)

label=Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)
signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)


window.mainloop()