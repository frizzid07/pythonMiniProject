from Tkinter import *

root = Tk()
root.title("Indian Cuisine Menu")

frame = Frame(root, bg="dark slate blue")
frame.grid()

lbl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Helvetica", 25), bg="dark slate blue", fg="springgreen")
lbl1.grid(column=1, columnspan=2)

lbl2 = Label(frame, text="Indian Cuisine", pady=5, font=("Helvetica", 20), bg="dark slate blue", fg="goldenrod", padx=20)
lbl2.grid(row=1, column=1, columnspan=2)

lbl3 = Label(frame, text="Item(s)", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
lbl3.grid(row=2)

lbl4 = Label(frame, text="Price()", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
lbl4.grid(row=2, column=1)

lbl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
lbl5.grid(row=2, column=2)

lbl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Helvetica", 18))
lbl6.grid(row=2, column=3)

category1 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue", font=("Helvetica", 15))
category1.grid(row=3, columnspan=4)

item1 = Label(frame, text="Veg. Kolhapuri", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item1.grid(row=4, sticky=W)

item2 = Label(frame, text="Veg. Jaipuri", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item2.grid(row=5, sticky=W)

item3 = Label(frame, text="Veg. Paneer Tikka Masala", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item3.grid(row=6, sticky=W)

item4 = Label(frame, text="Veg. Malai Kofta", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item4.grid(row=7, sticky=W)

item5 = Label(frame, text="Veg. Palak Paneer", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item5.grid(row=8, sticky=W)

item6 = Label(frame, text="Mix Vegetable", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item6.grid(row=9, sticky=W)

price1 = Label(frame, text="120.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price1.grid(row=4, column=1)

price2 = Label(frame, text="120.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price2.grid(row=5, column=1)

price3 = Label(frame, text="140.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price3.grid(row=6, column=1)

price4 = Label(frame, text="140.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price4.grid(row=7, column=1)

price5 = Label(frame, text="140.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price5.grid(row=8, column=1)

price6 = Label(frame, text="160.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price6.grid(row=9, column=1)

spin1 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin1.grid(row=4, column=3)

spin2 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin2.grid(row=5, column=3)

spin3 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin3.grid(row=6, column=3)

spin4 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin4.grid(row=7, column=3)

spin5 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin5.grid(row=8, column=3)

spin6 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin6.grid(row=9, column=3)

def normal1():
    spin1.config(state=NORMAL)
check1 = Checkbutton(frame, bg="dark slate blue", command=normal1, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check1.grid(row=4, column=2)

def normal2():
    spin2.config(state=NORMAL)
check2 = Checkbutton(frame, bg="dark slate blue", command=normal2, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check2.grid(row=5, column=2)

def normal3():
    spin3.config(state=NORMAL)
check3 = Checkbutton(frame, bg="dark slate blue", command=normal3, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check3.grid(row=6, column=2)

def normal4():
    spin4.config(state=NORMAL)
check4 = Checkbutton(frame, bg="dark slate blue", command=normal4, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check4.grid(row=7, column=2)

def normal5():
    spin5.config(state=NORMAL)
check5 = Checkbutton(frame, bg="dark slate blue", command=normal5, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check5.grid(row=8, column=2)

def normal6():
    spin6.config(state=NORMAL)
check6 = Checkbutton(frame, bg="dark slate blue", command=normal6, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check6.grid(row=9, column=2)

category2 = Label(frame, text="TANDOOR", padx=8, pady=5, fg="goldenrod", bg="dark slate blue", font=("Helvetica", 15))
category2.grid(row=10, columnspan=4)

item7 = Label(frame, text="Roti", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item7.grid(row=11, sticky=W)

item8 = Label(frame, text="Butter Roti", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item8.grid(row=12, sticky=W)

item9 = Label(frame, text="Butter Naan", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item9.grid(row=13, sticky=W)

item10 = Label(frame, text="Butter Kulcha", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
item10.grid(row=14, sticky=W)

price7 = Label(frame, text="15.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price7.grid(row=11, column=1)

price8 = Label(frame, text="25.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price8.grid(row=12, column=1)

price9 = Label(frame, text="35.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price9.grid(row=13, column=1)

price10 = Label(frame, text="35.00", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
price10.grid(row=14, column=1)

spin7 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin7.grid(row=11, column=3)

spin8 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin8.grid(row=12, column=3)

spin9 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin9.grid(row=13, column=3)

spin10 = Spinbox(frame, from_=1, to=10, state=DISABLED, width=10, bg="dark slate blue", disabledbackground="dark slate blue", fg="goldenrod", font=("Helvetica", 10), justify=CENTER)
spin10.grid(row=14, column=3)

def normal7():
    spin7.config(state=NORMAL)
check7 = Checkbutton(frame, bg="dark slate blue", command=normal7, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check7.grid(row=11, column=2)

def normal8():
    spin8.config(state=NORMAL)
check8 = Checkbutton(frame, bg="dark slate blue", command=normal8, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check8.grid(row=12, column=2)

def normal9():
    spin9.config(state=NORMAL)
check9 = Checkbutton(frame, bg="dark slate blue", command=normal9, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check9.grid(row=13, column=2)

def normal10():
    spin10.config(state=NORMAL)
check10 = Checkbutton(frame, bg="dark slate blue", command=normal10, pady=5, highlightcolor="goldenrod", selectcolor="springgreen")
check10.grid(row=14, column=2)

mainloop()