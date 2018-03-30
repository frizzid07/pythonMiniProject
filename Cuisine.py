from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Cuisine Selection")

cuisine = Frame(root, bg="dark slate gray")
cuisine.pack()

def cuisineMenu0():
	messagebox.showinfo("","Indian Cuisine")

def cuisineMenu1():
	messagebox.showinfo("","Italian Cuisine")
	
def cuisineMenu2():
	messagebox.showinfo("","Chinese Cuisine")
	
def cuisineMenu3():
	messagebox.showinfo("","Thai Cuisine")
	
btn1 = Button(cuisine,fg="springgreen",bg="dark slate gray",activebackground="springgreen",font=("Helvetica", 14),activeforeground="goldenrod",text="Indian Cuisine",command=cuisineMenu0)
btn1.grid(row=0,column=0)

btn2 = Button(cuisine,fg="springgreen",bg="dark slate gray",activebackground="springgreen",font=("Helvetica", 14),activeforeground="goldenrod",text="Italian Cuisine",command=cuisineMenu1)
btn2.grid(row=0,column=1)

btn3 = Button(cuisine,fg="springgreen",bg="dark slate gray",activebackground="springgreen",font=("Helvetica", 14),activeforeground="goldenrod",text="Chinese Cuisine",command=cuisineMenu2)
btn3.grid(row=1,column=0)

btn4 = Button(cuisine,fg="springgreen",bg="dark slate gray",activebackground="springgreen",font=("Helvetica", 14),activeforeground="goldenrod",text="Thai Cuisine",command=cuisineMenu3)
btn4.grid(row=1,column=1)

mainloop()