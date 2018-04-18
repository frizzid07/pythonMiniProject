from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os

with sqlite3.connect('projectDB.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()

class main:	
	
	def __init__(self,master):
		self.master = master
		self.username = StringVar()
		self.password = StringVar()
		self.widgets()	
	
	def login(self):
            with sqlite3.connect('projectDB.db') as db:
                 c = db.cursor()
            
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
            c.execute(find_user,[(self.username.get()),(self.password.get())])
            result = c.fetchall()
		
            if result:
                #filename = 'alt2.py'
                os.system("python alt2.py ")
                #root.destroy()

            else:
                ms.showerror('Oops!','Username Not Found.')
                self.username.set('')
                self.password.set('')
			
	def widgets(self):
		self.frame = Frame(self.master,bg="dark slate blue")
		Label(self.frame,text = 'WELCOME',font = ("Trebuchet MS",35),pady = 10, fg="goldenrod", bg="dark slate blue").grid()
		Label(self.frame, text="LUXURY ROYALE", font=("Trebuchet MS", 55), bg="dark slate blue", fg="springgreen", padx=20).grid(columnspan=3)
		Label(self.frame, text="Deluxe A/C Restaurant (Veg & Non-Veg)", font=("Trebuchet MS", 15), bg="dark slate blue", fg="goldenrod", pady=10).grid(columnspan=3)
		Label(self.frame, text="Cashier Login", font=("Trebuchet MS", 22), bg="dark slate blue", fg="springgreen", pady=25).grid(row=3, column=1, sticky=W)
		Label(self.frame, text="Cashier ID:", bg="dark slate blue", fg="goldenrod", font=("Trebuchet MS", 15), padx=-20, pady=15).grid(row=4, column=0, sticky=E)
		Label(self.frame, text="Password:", bg="dark slate blue", fg="goldenrod", font=("Trebuchet MS", 15), padx=-20, pady=25).grid(row=5, column=0, sticky=E)
		Entry(self.frame,textvariable = self.username,bd = 5,font = ('',15)).grid(row=4, column=1, sticky=E)
		Entry(self.frame, show="*",textvariable = self.password,bd = 5,font = ('',15)).grid(row=5, column=1, sticky=E)
		Button(self.frame, text="Login", font=("Trebuchet MS", 12), relief=RAISED, bg="dark slate blue", fg="goldenrod", cursor="cross", padx=30, pady=5, activebackground="springgreen",command=self.login, activeforeground="goldenrod").grid(row=6, columnspan=3)
		Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
		self.frame.grid()

if __name__ == '__main__':
    root = Tk()
    root.title('Restaurant Payment Method')
    main(root)
    root.mainloop()