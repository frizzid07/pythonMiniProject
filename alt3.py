from Tkinter import *
import os

class main:
	
	def __init__(self, master):
		self.master = master
		self.widgets()
		
	def callback(self):
		#filename = 'mainPage.py'
		os.system("python mainPage.py")
		#root.destroy()
	
	def widgets(self):
		self.frame = Frame(self.master, bg = "dark slate blue")
		Label(self.frame, text="SELECT CUISINE", fg="goldenrod", bg="dark slate blue", pady=10, font=("Helvetica", 25)).grid(columnspan=2)
		Button(self.frame, text="Indian", fg="springgreen",bg="dark slate blue",activebackground="springgreen",font=("Helvetica", 25),activeforeground="goldenrod", height=7, width=20, command=self.callback).grid(row=1)
		Button(self.frame, text="Chinese", fg="springgreen",bg="dark slate blue",activebackground="springgreen",font=("Helvetica", 25),activeforeground="goldenrod", height=7, width=20).grid(row=1, column=1)
		Button(self.frame, text="Italian", fg="springgreen",bg="dark slate blue",activebackground="springgreen",font=("Helvetica", 25),activeforeground="goldenrod", height=7, width=20).grid(row=2)
		Button(self.frame, text="Meditteranean", fg="springgreen",bg="dark slate blue",activebackground="springgreen",font=("Helvetica", 25),activeforeground="goldenrod", height=7, width=20).grid(row=2, column=1)
		self.frame.grid()

if __name__ == '__main__':
    root = Tk()
    root.title('Cuisine Selection')
    main(root)
    root.mainloop()	