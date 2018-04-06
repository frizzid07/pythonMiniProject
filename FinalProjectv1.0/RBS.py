from Tkinter import *
import tkMessageBox
import random
import time
import datetime

def indian():
    window = Toplevel(root1)
    window.title('INDIAN CUISINE')
    window.geometry("675x570")
    #ind = Frame(window,width=335,height=570)
    frame = Frame(window, bg="dark slate blue")
    frame.grid()
    global spin1,spin2,spin3,spin4,spin5,spin6,spin7,spin8,spin9,spin10
    lbl1 = Label(frame, text="Luxury Royale Restaurant", pady=5, font=("Helvetica", 25), bg="dark slate blue",
                 fg="springgreen")
    lbl1.grid(column=1, columnspan=2)

    lbl2 = Label(frame, text="Indian Cuisine", pady=5, font=("Helvetica", 20), bg="dark slate blue", fg="goldenrod",
                 padx=20)
    lbl2.grid(row=1, column=1, columnspan=2)

    lbl3 = Label(frame, text="Item(s)", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
    lbl3.grid(row=2)

    lbl4 = Label(frame, text="Price()", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
    lbl4.grid(row=2, column=1)

    lbl5 = Label(frame, text="Item\nSelection", fg="springgreen", pady=5, bg="dark slate blue", font=("Helvetica", 18))
    lbl5.grid(row=2, column=2)

    lbl6 = Label(frame, text="Quantity", fg="springgreen", padx=8, pady=5, bg="dark slate blue", font=("Helvetica", 18))
    lbl6.grid(row=2, column=3)

    category1 = Label(frame, text="MAIN COURSE", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Helvetica", 15))
    category1.grid(row=3, columnspan=4)

    item1 = Label(frame, text="Veg. Kolhapuri", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
    item1.grid(row=4, sticky=W)

    item2 = Label(frame, text="Veg. Jaipuri", fg="springgreen", bg="dark slate blue", font=("Helvetica", 12))
    item2.grid(row=5, sticky=W)

    item3 = Label(frame, text="Veg. Paneer Tikka Masala", fg="springgreen", bg="dark slate blue",
                  font=("Helvetica", 12))
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

    spin1 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check1)
    spin1.grid(row=4, column=3)

    spin2 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check2)
    spin2.grid(row=5, column=3)

    spin3 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check3)
    spin3.grid(row=6, column=3)

    spin4 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check4)
    spin4.grid(row=7, column=3)

    spin5 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check5)
    spin5.grid(row=8, column=3)

    spin6 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check6)
    spin6.grid(row=9, column=3)

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

    category2 = Label(frame, text="TANDOOR", padx=8, pady=5, fg="goldenrod", bg="dark slate blue",
                      font=("Helvetica", 15))
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

    spin7 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check7)
    spin7.grid(row=11, column=3)

    spin8 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check8)
    spin8.grid(row=12, column=3)

    spin9 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check9)
    spin9.grid(row=13, column=3)

    spin10 = Entry(frame, state=DISABLED, width=10, font=("Helvetica", 10), justify=CENTER, textvariable=E_check10)
    spin10.grid(row=14, column=3)

    check7 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var7)
    check7.grid(row=11, column=2)

    check8 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var8)
    check8.grid(row=12, column=2)

    check9 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                         selectcolor="springgreen", variable=var9)
    check9.grid(row=13, column=2)

    check10 = Checkbutton(frame, bg="dark slate blue", command=chkbutton_value, pady=5, highlightcolor="goldenrod",
                          selectcolor="springgreen", variable=var10)
    check10.grid(row=14, column=2)

    frame.pack()


# -----------------creating window---------------
root1 = Tk()
root1.geometry("1350x750")
root1.title("LUXURY ROYALE")
root1.configure(background="white")

# -----------------creating frames------------------
Tops = Frame(root1, width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)
f1 = Frame(root1, width=900, height=650, bd=8)
f1.pack(side=LEFT)
f2 = Frame(root1, width=440, height=650, bd=8)
f2.pack(side=RIGHT)

# ------------subpart of the frames---------------
f1a = Frame(f1, width=900, height=330, bd=8,)
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=6)
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width=440, height=450, bd=12)
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=250, bd=16)
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16)
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16)
f1ab.pack(side=RIGHT)

f1aaa = Frame(f1aa, width=400, height=165, bd=16, relief='raise')
f1aaa.pack(side=TOP)
f1aab = Frame(f1aa, width=400, height=165, bd=16, relief='raise')
f1aab.pack(side=BOTTOM)
f1aba = Frame(f1ab, width=400, height=165, bd=16, relief='raise')
f1aba.pack(side=TOP)
f1abb = Frame(f1ab, width=400, height=165, bd=16, relief='raise')
f1abb.pack(side=BOTTOM)

f2aa = Frame(f2a, width=450, height=330, bd=14)
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=14)
f2ab.pack(side=RIGHT)

# -----------------setting background colour---------------
Tops.configure(background='grey')
f1.configure(background='red')
f2.configure(background='red')

# -------------------creating labels-----------------------
lb1Info = Label(Tops, font=('Trebuchet MS', 50, 'bold'), text="LUXURY ROYALE", bd=10)
lb1Info.grid(row=0, column=0)


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

    POD = (ITEM1 * 120) + (ITEM2 * 120) + (ITEM3 * 140) + (ITEM4 * 140) + (ITEM5 * 140) + (ITEM6 * 160) + (ITEM7 * 15) + (ITEM9 * 25) + (ITEM9 * 35) + (ITEM10 * 35)

    DP = "Rs.", str('%.2f' % (POD))
    COD.set(DP)
    AA = "Rs.", str('%.2f' % (10))
    SC.set(AA)

    STOI = "Rs.", str('%.2f' % (POD + 10))
    ST.set(STOI)

    Tax = "Rs.", str('%.2f' % ((POD ) * (0.05)))
    PT.set(Tax)
    EX = (POD) * (0.05)
    TOC = "Rs.", str('%.2f' % (POD + 10 + EX))
    T.set(TOC)


# -----------------for receipt button---------------------
def Rcpt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 5000876)
    randomRef = str(x)
    Receipt_Ref = StringVar()
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t' + Receipt_Ref.get() + '\t' + DateOfOrder.get() + "\n")
    txtReceipt.insert(END, 'Items \t\t' + "Quantity\n")
    txtReceipt.insert(END, 'Veg.Kolhapuri: \t\t' + E_check1.get() + "\n")
    txtReceipt.insert(END, 'Veg.Jaipuri \t\t' + E_check2.get() + "\n")
    txtReceipt.insert(END, 'Paneer Tikka Masala: \t\t' + E_check3.get() + "\n")
    txtReceipt.insert(END, 'Malai Kofta: \t\t' + E_check4.get() + "\n")
    txtReceipt.insert(END, 'Palak Paneer: \t\t' + E_check5.get() + "\n")
    txtReceipt.insert(END, 'Mix Vegetable: \t\t' + E_check6.get() + "\n")
    txtReceipt.insert(END, 'Roti: \t\t' + E_check7.get() + "\n")
    txtReceipt.insert(END, 'Butter Roti: \t\t' + E_check8.get() + "\n")
    txtReceipt.insert(END, 'Butter Naan: \t\t' + E_check9.get() + "\n")
    txtReceipt.insert(END, 'Butter Kulcha: \t\t' + E_check10.get() + "\n")
    txtReceipt.insert(END, 'Cost Of Food:\t\t' + COD.get() + "\n" + 'Tax Paid:\t' + PT.get() + "\n")
    txtReceipt.insert(END, 'Sub Total:\t' + ST.get() + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t' + SC.get() + "\n" + 'Total Cost:\t' + T.get() + "\n")


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


DateOfOrder.set(time.strftime("%d/%m/%Y"))

# --------------------test butttons and frames---------------------------------
Button(f1aaa, text='INDIAN CUISINE', command=indian).pack()
#Button(f1aab, text='ITALIAN CUISINE', command=italian).pack()
#Button(f1aba, text='CHINESE CUISINE', command=chinese).pack()
#Button(f1abb, text='CONTINENTAL CUISINE', command=continental).pack()

# Similarly make italian,chinese,continental functions and paste your layout code in them







# --------------------creating receipt(creating labels)-------------
lb1Receipt = Label(ft2, font=('arial', 12, 'bold'), text="RECEIPT:", bd=2, anchor='w')
lb1Receipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

# -----------------------Price Information--------------------------
lb1COD = Label(f2aa, font=('arial', 12, 'bold'), text="COST OF DRINKS", bd=8, anchor='w')
lb1COD.grid(row=2, column=0, sticky=W)
txtCOD = Entry(f2aa, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=COD)
txtCOD.grid(row=2, column=1)

lb1COC = Label(f2aa, font=('arial', 12, 'bold'), text="COST OF CAKES", bd=8, anchor='w')
lb1COC.grid(row=3, column=0, sticky=W)
txtCOC = Entry(f2aa, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=COC)
txtCOC.grid(row=3, column=1)

lb1SC = Label(f2aa, font=('arial', 12, 'bold'), text="SERVICE CHARGE", bd=8, anchor='w')
lb1SC.grid(row=4, column=0, sticky=W)
txtSC = Entry(f2aa, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=SC)
txtSC.grid(row=4, column=1)

# ---------------------Payment Options---------------------------
lb1PT = Label(f2ab, font=('arial', 12, 'bold'), text="GST", bd=8, anchor='w')
lb1PT.grid(row=2, column=0, sticky=W)
txtPT = Entry(f2ab, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=PT)
txtPT.grid(row=2, column=1)

lb1ST = Label(f2ab, font=('arial', 12, 'bold'), text="SUB TOTAL", bd=8, anchor='w')
lb1ST.grid(row=3, column=0, sticky=W)
txtST = Entry(f2ab, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=ST)
txtST.grid(row=3, column=1)

lb1T = Label(f2ab, font=('arial', 12, 'bold'), text="TOTAL", bd=8, anchor='w')
lb1T.grid(row=4, column=0, sticky=W)
txtT = Entry(f2ab, font=('arial', 12, 'bold'), bd=8, insertwidth=2, justify='left', textvariable=T)
txtT.grid(row=4, column=1)

# -----------------------creating buttons--------------------------
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 11, 'bold'), width=1, text="TOTAL",
                  command=COI).grid(row=0, column=0)

btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 11, 'bold'), width=3, text="RECEIPT",
                    command=Rcpt).grid(row=0, column=1)

btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 11, 'bold'), width=2, text="RESET",
                  command=Reset).grid(row=0, column=2)

btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 11, 'bold'), width=2, text="EXIT",
                 command=qExit).grid(row=0, column=3)

root1.mainloop()