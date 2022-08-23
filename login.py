from tkinter import *
from tkinter import messagebox
import sqlite3
import os


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Inventory System EdivetPlus Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.img = PhotoImage(file='images/login.png')
        Label(root, image=self.img, bg="white").place(x=50, y=50)

        self.frame = Frame(root, width=350, height=350, bg='white')
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text="Sign in", fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        #######################------------------username----------------
        self.username = StringVar()
        self.password = StringVar()

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')

        user = Entry(self.frame, textvariable=self.username, width=25, fg='black', border=0, bg='white',
                     font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'ID')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(self.frame, width=295, height=2, bg='black', ).place(x=25, y=107)

        ######################--------------------password------------------
        def on_enterP(e):
            password.delete(0, 'end')

        def on_leaveP(e):
            name = password.get()
            if name == '':
                password.insert(0, 'Pin')

        password = Entry(self.frame, textvariable=self.password, width=25, fg='black', border=0, bg='white',
                         font=('Microsoft YaHei UI Light', 11))
        password.place(x=30, y=150)
        password.insert(0, 'Pin')
        password.bind('<FocusIn>', on_enterP)
        password.bind('<FocusOut>', on_leaveP)

        Frame(self.frame, width=295, height=2, bg='black', ).place(x=25, y=177)
        ######################--------------------------------------------------------

        Button(self.frame, command=self.login, width=39, pady=7, text='Sing In', bg='#57a1f8', fg='white',
               border=0).place(x=35, y=204)

        label = Label(self.frame, text="dont have an account?", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)
        sing_up = Button(self.frame, command=self.createAcc, width=6, text="Sing up", border=0, bg='white',
                         cursor='hand2', fg='#57a1f8')
        sing_up.place(x=215, y=270)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All filds are requaierd", parent=self.root)
            else:
                cur.execute("select * from users where Name=? AND password=?",
                            (self.username.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid username or password", parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python main.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def createAcc(self):
        self.root.destroy()
        os.system("python signup.py")


root = Tk()
obj = Login(root)
root.mainloop()
