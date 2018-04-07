from tkinter import *
import os

class main:
	
	def __init__(self, master):
		self.master = master
		self.username = StringVar()
		self.username = "tanmay"
		self.password = StringVar()
		self.widgets()
	
	def callback(self):
		os.system("python RBS.py")
	
	def widgets(self):
		self.frame = Frame(self.master, bg="dark slate blue")
		Label(self.frame, text="Logged in as " + self.username + "...", pady = 10, font=('Trebuchet MS', 12), fg="goldenrod", bg="dark slate blue").grid(columnspan=4)
		Label(self.frame, text="SELECT TABLE TO PROCEED", pady = 10, font=('Trebuchet MS', 22), fg="goldenrod", bg="dark slate blue").grid(columnspan=4)
		k=1
		for i in range(4):
			for j in range(2,5):
				Button(self.frame,fg="springgreen",bg="dark slate blue",activebackground="springgreen",font=("Trebuchet MS", 22),activeforeground="goldenrod",padx=55,pady=55,text="Table %d" % (k), command=self.callback).grid(row=j, column=i)
				k+=1
		self.frame.grid()

if __name__ == '__main__':
    root1 = Tk()
    root1.title('Table Selection')
    main(root1)
    root1.mainloop()