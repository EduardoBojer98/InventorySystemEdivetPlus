from tkinter import *
from tkinter import messagebox
import os
import sqlite3

class signup:
    def __init__(self, root):
        self.root = root
        self.root.title('Inventory System EdivetPlus Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.img = PhotoImage(file='images/singup.png')
        Label(root, image=self.img, bg="white").place(x=50, y=50)

        frame = Frame(root, width=350, height=350, bg='white')
        frame.place(x=480, y=70)

        heading = Label(frame, text="Sign up", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.username = StringVar()
        self.password = StringVar()
        self.userID = StringVar()

        #######################------------------username----------------
        def on_enter(e):
            iduser.delete(0, 'end')

        def on_leave(e):
            name = iduser.get()
            if name == '':
                iduser.insert(0, 'ID')

        iduser = Entry(frame,textvariable=self.userID, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        iduser.place(x=30, y=80)
        iduser.insert(0, 'ID')
        iduser.bind('<FocusIn>', on_enter)
        iduser.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=107)

        ######################--------------------password------------------
        def on_enterP(e):
            username.delete(0, 'end')

        def on_leaveP(e):
            name = username.get()
            if name == '':
                username.insert(0, 'Name')

        username = Entry(frame,textvariable=self.username, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        username.place(x=30, y=150)
        username.insert(0, 'Name')
        username.bind('<FocusIn>', on_enterP)
        username.bind('<FocusOut>', on_leaveP)

        Frame(frame, width=295, height=2, bg='black', ).place(x=25, y=177)

        ########################################################################################
        def on_enterPR(e):
            pin.delete(0, 'end')

        def on_leavePR(e):
            name = pin.get()
            if name == '':
                pin.insert(0, 'Password')

        pin = Entry(frame, width=25,textvariable=self.password, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        pin.place(x=30, y=220)
        pin.insert(0, 'Password')
        pin.bind('<FocusIn>', on_enterPR)
        pin.bind('<FocusOut>', on_leavePR)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
        ######################--------------------------------------------------------

        Button(frame,command=self.adduser, width=39, pady=7, text='Sing In', bg='#57a1f8', fg='white', border=0).place(x=35, y=260)

        label = Label(frame, text="dont have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=305)

        sing_up = Button(frame,command=self.gotoLogin, width=6, text="Sing up", border=0, bg='white', cursor='hand2', fg='#57a1f8')
        sing_up.place(x=215, y=305)

    def adduser(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.userID.get() == "":
                messagebox.showerror("Error", "User ID is required", parent=self.root)
            else:
                cur.execute("Select * from users where userID=?", (self.userID.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This user ID already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into users (userID,Name,password) values(?,?,?)", (
                        self.userID.get(),
                        self.username.get(),
                        self.password.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', "User added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def gotoLogin(self):
        self.root.destroy()
        os.system("python login.py")


root = Tk()
obj = signup(root)
root.mainloop()
