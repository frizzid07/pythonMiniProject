from tkinter import *

root = Tk()
root.title("Restaurant Billing System")

frame = Frame(root, bg="dark slate blue")
frame.grid()

lbl1 = Label(frame, text="Welcome to...", font=("Helvetica", 15), bg="dark slate blue", fg="goldenrod", pady=20)
lbl1.grid(columnspan=3)

lbl2 = Label(frame, text="LUXURY ROYALE", font=("Helvetica", 55), bg="dark slate blue", fg="springgreen", padx=20)
lbl2.grid(columnspan=3)

lbl3 = Label(frame, text="Deluxe A/C Restaurant (Veg & Non-Veg)", font=("Helvetica", 15), bg="dark slate blue", fg="goldenrod", pady=10)
lbl3.grid(columnspan=3)

lbl4 = Label(frame, text="Cashier Login", font=("Helvetica", 22), bg="dark slate blue", fg="springgreen", pady=25)
lbl4.grid(row=3, column=1, sticky=W)

lbl5 = Label(frame, text="Cashier ID:", bg="dark slate blue", fg="goldenrod", font=("Helvetica", 15), padx=-20, pady=15)
lbl5.grid(row=4, column=0, sticky=E)

lbl6 = Label(frame, text="Password:", bg="dark slate blue", fg="goldenrod", font=("Helvetica", 15), padx=-20, pady=25)
lbl6.grid(row=5, column=0, sticky=E)

ent1 = Entry(frame)
ent1.grid(row=4, column=1, sticky=E)

ent2 = Entry(frame, show="*")
ent2.grid(row=5, column=1, sticky=E)

btn1 = Button(frame, text="Login", font=("Helvetica", 12), relief=RAISED, bg="dark slate blue", fg="goldenrod", cursor="cross", padx=30, pady=5, activebackground="springgreen", activeforeground="goldenrod")
btn1.grid(row=6, columnspan=3)

lbl7 = Label(frame, text=" ", bg="dark slate blue")
lbl7.grid(row=7)

root.mainloop()
