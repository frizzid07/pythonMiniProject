from tkinter import *
from tkinter import messagebox
import random
import time
import datetime

def indian():
    window = Toplevel(root1)
    window.title('INDIAN CUISINE')
    #window.geometry("675x570")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10,spin11,spin12,spin13,spin14
    labl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Trebuchet MS", 25), bg="dark slate blue",
                 fg="springgreen")
    labl1.grid(column=1, columnspan=2)

    labl2 = Label(frame, text="Indian Cuisine", pady=5, font=("Trebuchet MS", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    labl2.grid(row=1, column=1, columnspan=2)

    labl3 = Label(frame, text="Items", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl3.grid(row=2)

    labl4 = Label(frame, text="Price(₹)", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl4.grid(row=2, column=1)

    labl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl5.grid(row=2, column=2)

    labl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Trebuchet MS", 18))
    labl6.grid(row=2, column=3)

    category1 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category1.grid(row=3, columnspan=4)

    item1 = Label(frame, text="Veg. Kolhapuri", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item1.grid(row=4, sticky=W)

    item2 = Label(frame, text="Veg. Jaipuri", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item2.grid(row=5, sticky=W)

    item3 = Label(frame, text="Paneer Tikka Masala", fg="springgreen", bg="dark slate blue",
                  font=("Trebuchet MS", 12))
    item3.grid(row=6, sticky=W)

    item4 = Label(frame, text="Veg. Malai Kofta", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item4.grid(row=7, sticky=W)

    item5 = Label(frame, text="Veg. Palak Paneer", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item5.grid(row=8, sticky=W)

    item6 = Label(frame, text="Mix Vegetable", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item6.grid(row=9, sticky=W)

    Label(frame, text="Spl. Chicken Curry", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, sticky=W)
	
    Label(frame, text="Spl. Fish Fry (2 pcs)", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, sticky=W)
	
    Label(frame, text="Spl. Fish Curry", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, sticky=W)
	
    Label(frame, text="Spl. Mutton Korma", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, sticky=W)
	
    price1 = Label(frame, text="180.00", pady=5, fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price1.grid(row=4, column=1)

    price2 = Label(frame, text="180.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price2.grid(row=5, column=1)

    price3 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price3.grid(row=6, column=1)

    price4 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price4.grid(row=7, column=1)

    price5 = Label(frame, text="200.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price5.grid(row=8, column=1)

    price6 = Label(frame, text="220.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price6.grid(row=9, column=1)

    Label(frame, text="240.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=10, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=11, column=1)

    Label(frame, text="260.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=12, column=1)

    Label(frame, text="290.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12)).grid(row=13, column=1)
	
    spin1 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check1)
    spin1.grid(row=4, column=3)

    spin2 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check2)
    spin2.grid(row=5, column=3)

    spin3 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check3)
    spin3.grid(row=6, column=3)

    spin4 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check4)
    spin4.grid(row=7, column=3)

    spin5 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check5)
    spin5.grid(row=8, column=3)

    spin6 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check6)
    spin6.grid(row=9, column=3)
	
    spin7 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check7)
    spin7.grid(row=10, column=3)

    spin8 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check8)
    spin8.grid(row=11, column=3)

    spin9 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check9)
    spin9.grid(row=12, column=3)

    spin10 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check10)
    spin10.grid(row=13, column=3)

    check1 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var1)
    check1.grid(row=4, column=2)

    check2 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var2)
    check2.grid(row=5, column=2)

    check3 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var3)
    check3.grid(row=6, column=2)

    check4 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var4)
    check4.grid(row=7, column=2)

    check5 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var5)
    check5.grid(row=8, column=2)

    check6 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var6)
    check6.grid(row=9, column=2)
	
    check7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var7)
    check7.grid(row=10, column=2)

    check8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var8)
    check8.grid(row=11, column=2)

    check9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var9)
    check9.grid(row=12, column=2)

    check10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var10)
    check10.grid(row=13, column=2)

    category2 = Label(frame, text="TANDOOR", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Trebuchet MS", 15))
    category2.grid(row=14, columnspan=4)

    item7 = Label(frame, text="Roti", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item7.grid(row=15, sticky=W)

    item8 = Label(frame, text="Butter Roti", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item8.grid(row=16, sticky=W)

    item9 = Label(frame, text="Butter Naan", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item9.grid(row=17, sticky=W)

    item10 = Label(frame, text="Butter Kulcha", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    item10.grid(row=18, sticky=W)

    price7 = Label(frame, text="30.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price7.grid(row=15, column=1)

    price8 = Label(frame, text="40.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price8.grid(row=16, column=1)

    price9 = Label(frame, text="45.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price9.grid(row=17, column=1)

    price10 = Label(frame, text="55.00", fg="springgreen", bg="dark slate blue", font=("Trebuchet MS", 12))
    price10.grid(row=18, column=1)

    spin11 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check11)
    spin11.grid(row=15, column=3)

    spin12 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check12)
    spin12.grid(row=16, column=3)

    spin13 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check13)
    spin13.grid(row=17, column=3)

    spin14 = Spinbox(frame, from_=0, to=10, state=DISABLED, width=10, font=("Trebuchet MS", 10), justify=CENTER, textvariable=E_check14)
    spin14.grid(row=18, column=3)

    check11 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var11)
    check11.grid(row=15, column=2)

    check12 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var12)
    check12.grid(row=16, column=2)

    check13 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var13)
    check13.grid(row=17, column=2)

    check14 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=var14)
    check14.grid(row=18, column=2)
	
    def hide():
	    window.withdraw()
    btn1 = Button(frame, bg="dark slate blue", command=hide, padx=5, fg="springgreen", activebackground="springgreen",font=("Trebuchet MS", 12),activeforeground="goldenrod", text="PROCEED").grid(row=19, columnspan=4)
    labltp = Label(frame, text="", bg="dark slate blue").grid(row=20, columnspan=4)
    frame.pack()


# -----------------creating window---------------
root1 = Tk()
root1.geometry("1350x750")
root1.title("LUXURY ROYALE")
root1.configure(background="dark slate blue")

# -----------------creating frames------------------
Tops = Frame(root1, bg="dark slate blue", width=1350, height=75, bd=14)
Tops.pack(side=TOP)
f1 = Frame(root1, bg="dark slate blue", width=900, height=650, bd=8)
f1.pack(side=LEFT)
f2 = Frame(root1, bg="dark slate blue", width=440, height=650, bd=8)
f2.pack(side=RIGHT)

# ------------subpart of the frames---------------
f1a = Frame(f1, bg="dark slate blue", width=900, height=330, bd=8,)
f1a.pack(side=TOP)
f2a = Frame(f1, bg="dark slate blue", width=900, height=320, bd=6)
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, bg="dark slate blue", width=300, height=400, bd=12)
ft2.pack(side=TOP)
fb2 = Frame(f2, bg="dark slate blue", width=440, height=250, bd=16)
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, bg="dark slate blue", width=400, height=330, bd=16)
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, bg="dark slate blue", width=400, height=330, bd=16)
f1ab.pack(side=RIGHT)

f1aaa = Frame(f1aa, width=400, height=165,bg="dark slate blue",  bd=16)
f1aaa.pack(side=TOP)
f1aab = Frame(f1aa, width=400, height=165, bd=16, bg="dark slate blue")
f1aab.pack(side=BOTTOM)
f1aba = Frame(f1ab, width=400, height=165, bd=16, bg="dark slate blue")
f1aba.pack(side=TOP)
f1abb = Frame(f1ab, width=400, height=165, bd=16, bg="dark slate blue")
f1abb.pack(side=BOTTOM)

f2aa = Frame(f2a, width=450, height=330, bg="dark slate blue", bd=14)
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bg="dark slate blue", bd=14)
f2ab.pack(side=RIGHT)

# -----------------setting background colour---------------
#Tops.configure(background='dark slate blue')
#f1.configure(background='dark slate blue')
#f2.configure(background='dark slate blue')

# -------------------creating labels-----------------------
lb1Info = Label(Tops, font=('Trebuchet MS', 45, 'bold'), bg="dark slate blue", fg="goldenrod", text="LUXURY ROYALE", bd=5)
lb1Info.grid()
Label(Tops, text="Deluxe A/C Restaurant (Veg & Non-Veg)", font=("Trebuchet MS", 15), bg="dark slate blue", fg="goldenrod").grid(row=1)
Label(Tops, text="--------------------------------------------------------------------------------------------------------------------------------------------------------", font=("Trebuchet MS", 15), bg="dark slate blue", fg="goldenrod").grid(row=2)
# -------------------for exit button------------------

def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root1.destroy()
        return


# ------------------for reset button------------------

def Reset():
    txtReceipt.delete("1.0", END)
    COD.set("")
    COC.set("")
    PT.set("")
    SC.set("")
    T.set("")
    ST.set("")

    E_check1.set("0")
    E_check2.set("0")
    E_check3.set("0")
    E_check4.set("0")
    E_check5.set("0")
    E_check6.set("0")
    E_check7.set("0")
    E_check8.set("0")
    E_check9.set("0")
    E_check10.set("0")
    E_check11.set("0")
    E_check12.set("0")
    E_check13.set("0")
    E_check14.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")

    spin1.configure(state=DISABLED)
    spin2.configure(state=DISABLED)
    spin3.configure(state=DISABLED)
    spin4.configure(state=DISABLED)
    spin5.configure(state=DISABLED)
    spin6.configure(state=DISABLED)
    spin7.configure(state=DISABLED)
    spin8.configure(state=DISABLED)
    spin9.configure(state=DISABLED)
    spin10.configure(state=DISABLED)
    spin11.configure(state=DISABLED)
    spin12.configure(state=DISABLED)
    spin13.configure(state=DISABLED)
    spin14.configure(state=DISABLED)


# ---------------checkbutton changes-----------------

def chkbutton_value():
    if (var1.get() == 1):
        spin1.configure(state=NORMAL)
    elif var1.get() == 0:
        spin1.configure(state=DISABLED)
        E_check1.set("0")

    if (var2.get() == 1):
        spin2.configure(state=NORMAL)
    elif var2.get() == 0:
        spin2.configure(state=DISABLED)
        E_check2.set("0")

    if (var3.get() == 1):
        spin3.configure(state=NORMAL)
    elif var3.get() == 0:
        spin3.configure(state=DISABLED)
        E_check3.set("0")

    if (var4.get() == 1):
        spin4.configure(state=NORMAL)
    elif var4.get() == 0:
        spin4.configure(state=DISABLED)
        E_check4.set("0")

    if (var5.get() == 1):
        spin5.configure(state=NORMAL)
    elif var5.get() == 0:
        spin5.configure(state=DISABLED)
        E_check5.set("0")

    if (var6.get() == 1):
        spin6.configure(state=NORMAL)
    elif var6.get() == 0:
        spin6.configure(state=DISABLED)
        E_check6.set("0")

    if (var7.get() == 1):
        spin7.configure(state=NORMAL)
    elif var7.get() == 0:
        spin7.configure(state=DISABLED)
        E_check7.set("0")

    if (var8.get() == 1):
        spin8.configure(state=NORMAL)
    elif var8.get() == 0:
        spin8.configure(state=DISABLED)
        E_check8.set("0")

    if (var9.get() == 1):
        spin9.configure(state=NORMAL)
    elif var9.get() == 0:
        spin9.configure(state=DISABLED)
        E_check9.set("0")

    if (var10.get() == 1):
        spin10.configure(state=NORMAL)
    elif var10.get() == 0:
        spin10.configure(state=DISABLED)
        E_check10.set("0")

    if (var11.get() == 1):
        spin11.configure(state=NORMAL)
    elif var11.get() == 0:
        spin11.configure(state=DISABLED)
        E_check11.set("0")
	
    if (var12.get() == 1):
        spin12.configure(state=NORMAL)
    elif var12.get() == 0:
        spin12.configure(state=DISABLED)
        E_check12.set("0")
		
    if (var13.get() == 1):
        spin13.configure(state=NORMAL)
    elif var13.get() == 0:
        spin13.configure(state=DISABLED)
        E_check13.set("0")
		
    if (var14.get() == 1):
        spin14.configure(state=NORMAL)
    elif var14.get() == 0:
        spin14.configure(state=DISABLED)
        E_check14.set("0")

# ----------------for TOTAL button--------------------------
def COI():
    ITEM1 = float(E_check1.get())
    ITEM2 = float(E_check2.get())
    ITEM3 = float(E_check3.get())
    ITEM4 = float(E_check4.get())
    ITEM5 = float(E_check5.get())
    ITEM6 = float(E_check6.get())
    ITEM7 = float(E_check7.get())
    ITEM8 = float(E_check8.get())
    ITEM9 = float(E_check9.get())
    ITEM10 = float(E_check10.get())
    ITEM11 = float(E_check11.get())
    ITEM12 = float(E_check12.get())
    ITEM13 = float(E_check13.get())
    ITEM14 = float(E_check14.get())
	
    POD = (ITEM1 * 180) + (ITEM2 * 180) + (ITEM3 * 200) + (ITEM4 * 200) + (ITEM5 * 200) + (ITEM6 * 220) + (ITEM7 * 240) + (ITEM8 * 260) + (ITEM9 * 260) + (ITEM10 * 290) + (ITEM11 * 30) + (ITEM12 * 40) + (ITEM13 * 45) + (ITEM14 * 55)
	
    GST = POD * 0.025
    DP = "₹", str('%.2f' % (POD))
    COD.set(DP)
    AA = "₹", str('%.2f' % ((POD ) * (0.025)))
    SC.set(AA)

    '''STOI = "Rs.", str('%.2f' % (POD + 10))
    ST.set(STOI)'''

    Tax = "₹", str('%.2f' % ((POD ) * (0.025)))
    PT.set(Tax)
    EX = POD + 2*(GST)
    TOC = "₹", str('%.2f' % (EX))
    T.set(TOC)


# -----------------for receipt button---------------------
def Rcpt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 5000876)
    randomRef = str(x)
    Receipt_Ref = StringVar()
    Receipt_Ref.set("BILL" + randomRef)
	
    txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\t\tDate:' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Items \t\t\t' + "Quantity\n")
    txtReceipt.insert(END, 'Veg.Kolhapuri: \t\t\t' + E_check1.get() + "\n")
    txtReceipt.insert(END, 'Veg.Jaipuri \t\t\t' + E_check2.get() + "\n")
    txtReceipt.insert(END, 'Paneer Tikka Masala: \t\t\t' + E_check3.get() + "\n")
    txtReceipt.insert(END, 'Malai Kofta: \t\t\t' + E_check4.get() + "\n")
    txtReceipt.insert(END, 'Palak Paneer: \t\t\t' + E_check5.get() + "\n")
    txtReceipt.insert(END, 'Mix Vegetable: \t\t\t' + E_check6.get() + "\n")
    txtReceipt.insert(END, 'Spl. Chicken Curry: \t\t\t' + E_check7.get() + "\n")
    txtReceipt.insert(END, 'Spl. Fish Fry (2 pcs): \t\t\t' + E_check8.get() + "\n")
    txtReceipt.insert(END, 'Spl. Fish Curry: \t\t\t' + E_check9.get() + "\n")
    txtReceipt.insert(END, 'Spl. Mutton Korma: \t\t\t' + E_check10.get() + "\n")
    txtReceipt.insert(END, 'Roti: \t\t\t' + E_check11.get() + "\n")
    txtReceipt.insert(END, 'Butter Roti: \t\t\t' + E_check12.get() + "\n")
    txtReceipt.insert(END, 'Butter Naan: \t\t\t' + E_check13.get() + "\n")
    txtReceipt.insert(END, 'Butter Kulcha: \t\t\t' + E_check14.get() + "\n")
    txtReceipt.insert(END, 'Sub Total:\t\t\t' + COD.get() + "\n" + 'CGST(2.5%):\t\t\t' + SC.get() + "\n")
    txtReceipt.insert(END, 'SGST(2.5%):\t\t\t' + PT.get() + "\n" + 'Total:\t\t\t' + T.get() + "\n")
    #txtReceipt.insert(END, 'Service Charge:\t\t\t' + SC.get() + "\n" + 'Total Cost:\t\t\t' + T.get() + "\n")


# -------------------variables required for program-----------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()

DateOfOrder = StringVar()
Receipt = StringVar()
COD = StringVar()
COC = StringVar()
PT = StringVar()
SC = StringVar()
T = StringVar()
ST = StringVar()

E_check1 = StringVar()
E_check2 = StringVar()
E_check3 = StringVar()
E_check4 = StringVar()
E_check5 = StringVar()
E_check6 = StringVar()
E_check7 = StringVar()
E_check8 = StringVar()
E_check9 = StringVar()
E_check10 = StringVar()
E_check11 = StringVar()
E_check12 = StringVar()
E_check13 = StringVar()
E_check14 = StringVar()


E_check1.set("0")
E_check2.set("0")
E_check3.set("0")
E_check4.set("0")
E_check5.set("0")
E_check6.set("0")
E_check7.set("0")
E_check8.set("0")
E_check9.set("0")
E_check10.set("0")
E_check11.set("0")
E_check12.set("0")
E_check13.set("0")
E_check14.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))

# --------------------test butttons and frames---------------------------------
Button(f1aaa, text='INDIAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=indian).pack()
Button(f1aab, text='ITALIAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=indian).pack()
Button(f1aba, text='CHINESE CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=indian).pack()
Button(f1abb, text='MEDITERRANEAN CUISINE', fg="springgreen",activebackground="springgreen",font=("Trebuchet MS", 14),activeforeground="goldenrod", relief=RAISED, bg="dark slate blue", cursor='cross', height=4, width=30, command=indian).pack()

# Similarly make italian,chinese,continental functions and paste your layout code in them







# --------------------creating receipt(creating labels)-------------
lb1Receipt = Label(ft2, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="RECEIPT:", bd=2, anchor='w')
lb1Receipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=40, height=18, bg="white", bd=4, font=('Trebuchet MS', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

# -----------------------Price Information--------------------------
lb1COD = Label(f2aa, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="SUB TOTAL:", bd=8, anchor='w')
lb1COD.grid(row=2, column=0, sticky=W)
txtCOD = Entry(f2aa, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=COD)
txtCOD.grid(row=2, column=1)

'''lb1COC = Label(f2aa, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="COST OF CAKES", bd=8, anchor='w')
lb1COC.grid(row=3, column=0, sticky=W)
txtCOC = Entry(f2aa, font=('Trebuchet MS', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=COC)
txtCOC.grid(row=3, column=1)'''

lb1SC = Label(f2aa, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="CGST(2.5%):", bd=8, anchor='w')
lb1SC.grid(row=3, column=0, sticky=W)
txtSC = Entry(f2aa, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=SC)
txtSC.grid(row=3, column=1)

# ---------------------Payment Options---------------------------
lb1PT = Label(f2ab, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="SGST(2.5%):", bd=8, anchor='w')
lb1PT.grid(row=2, column=0, sticky=W)
txtPT = Entry(f2ab, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=PT)
txtPT.grid(row=2, column=1)

'''lb1ST = Label(f2ab, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="SUB TOTAL", bd=8, anchor='w')
lb1ST.grid(row=3, column=0, sticky=W)
txtST = Entry(f2ab, font=('Trebuchet MS', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=ST)
txtST.grid(row=3, column=1)'''

lb1T = Label(f2ab, font=('Trebuchet MS', 12, 'bold'), bg="dark slate blue", text="TOTAL:", bd=8, anchor='w')
lb1T.grid(row=4, column=0, sticky=W)
txtT = Entry(f2ab, font=('Trebuchet MS', 12, 'bold'), bd=4, justify='left', textvariable=T)
txtT.grid(row=4, column=1)

# -----------------------creating buttons--------------------------
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="TOTAL",
                  command=COI).grid(row=0, column=0)

btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="RECEIPT",
                    command=Rcpt).grid(row=0, column=1)

btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="RESET",
                  command=Reset).grid(row=0, column=2)

btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", bg="dark slate blue", font=('Trebuchet MS', 11, 'bold'), width=4, text="EXIT",
                 command=qExit).grid(row=0, column=3)

root1.mainloop()