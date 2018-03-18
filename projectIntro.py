from tkinter import *

root = Tk()
root.title("Restaurant Billing System")

canvas = Canvas(bg="dark slate gray")
canvas.grid()

lbl1 = Label(canvas, text="Welcome to...", font=("Helvetica", 15), bg="dark slate gray", fg="goldenrod", pady=20)
lbl1.grid(columnspan=3)

lbl2 = Label(canvas, text="LUXURY ROYALE", font=("Helvetica", 55), bg="dark slate gray", fg="springgreen", padx=20)
lbl2.grid(columnspan=3)

lbl3 = Label(canvas, text="Deluxe A/C Restaurant (Veg & Non-Veg)", font=("Helvetica", 15), bg="dark slate gray", fg="goldenrod", pady=10)
lbl3.grid(columnspan=3)

lbl4 = Label(canvas, text="Cashier Login", font=("Helvetica", 22), bg="dark slate gray", fg="springgreen", pady=25)
lbl4.grid(row=3, column=1, sticky=W)

lbl5 = Label(canvas, text="Cashier ID:", bg="dark slate gray", fg="goldenrod", font=("Helvetica", 15), padx=-20, pady=15)
lbl5.grid(row=4, column=0, sticky=E)

lbl6 = Label(canvas, text="Password:", bg="dark slate gray", fg="goldenrod", font=("Helvetica", 15), padx=-20, pady=25)
lbl6.grid(row=5, column=0, sticky=E)

ent1 = Entry(canvas)
ent1.grid(row=4, column=1, sticky=E)

ent2 = Entry(canvas, show="*")
ent2.grid(row=5, column=1, sticky=E)

btn1 = Button(canvas, text="Login", font=("Helvetica", 12), bg="dark slate gray", fg="goldenrod", cursor="cross", padx=30, pady=5)
btn1.grid(row=6, columnspan=3)

root.mainloop()