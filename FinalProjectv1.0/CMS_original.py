from Tkinter import *
import tkMessageBox
import random
import time
import datetime

# -----------------creating window---------------
root1 = Tk()
root1.geometry("1350x750")
root1.title("LUXURY RESTRAURANT")
root1.configure(background='white')

# -----------------creating frames------------------
Tops = Frame(root1, width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)
f1 = Frame(root1, width=900, height=650, bd=8)
f1.pack(side=LEFT)
f2 = Frame(root1, width=440, height=650, bd=8)
f2.pack(side=RIGHT)

# ------------subpart of the frames---------------
f1a = Frame(f1, width=900, height=330, bd=8)
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

f2aa = Frame(f2a, width=450, height=330, bd=14)
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=14)
f2ab.pack(side=RIGHT)

# -----------------setting background colour---------------
Tops.configure(background='grey')
f1.configure(background='red')
f2.configure(background='red')

# -------------------creating labels-----------------------
lb1Info = Label(Tops, font=('Trebuchet MS', 50, 'bold'), text="LUXURY RESTAURANT", bd=10)
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

    E_COCO_COLA.set("0")
    E_PEPSI.set("0")
    E_FANTA.set("0")
    E_SPRITE.set("0")
    E_APPY.set("0")

    E_BROWNIE.set("0")
    E_BLACKFOREST_CAKE.set("0")
    E_REDVELVET_CAKE.set("0")
    E_RAINBOW_CAKE.set("0")
    E_BUTTERSCOTCH_CAKE.set("0")

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

    txtCOCO_COLA.configure(state=DISABLED)
    txtPEPSI.configure(state=DISABLED)
    txtFANTA.configure(state=DISABLED)
    txtSPRITE.configure(state=DISABLED)
    txtAPPY.configure(state=DISABLED)
    txtBROWNIE.configure(state=DISABLED)
    txtBLACKFOREST_CAKE.configure(state=DISABLED)
    txtREDVELVET_CAKE.configure(state=DISABLED)
    txtRAINBOW_CAKE.configure(state=DISABLED)
    txtBUTTERSCOTCH_CAKE.configure(state=DISABLED)


# ---------------checkbutton changes-----------------

def chkbutton_value():
    if (var1.get() == 1):
        txtCOCO_COLA.configure(state=NORMAL)
    elif var1.get() == 0:
        txtCOCO_COLA.configure(state=DISABLED)
        E_COCO_COLA.set("0")

    if (var2.get() == 1):
        txtPEPSI.configure(state=NORMAL)
    elif var2.get() == 0:
        txtPEPSI.configure(state=DISABLED)
        E_PEPSI.set("0")

    if (var3.get() == 1):
        txtFANTA.configure(state=NORMAL)
    elif var3.get() == 0:
        txtFANTA.configure(state=DISABLED)
        E_FANTA.set("0")

    if (var4.get() == 1):
        txtSPRITE.configure(state=NORMAL)
    elif var4.get() == 0:
        txtSPRITE.configure(state=DISABLED)
        E_SPRITE.set("0")

    if (var5.get() == 1):
        txtAPPY.configure(state=NORMAL)
    elif var5.get() == 0:
        txtAPPY.configure(state=DISABLED)
        E_APPY.set("0")

    if (var6.get() == 1):
        txtBROWNIE.configure(state=NORMAL)
    elif var6.get() == 0:
        txtBROWNIE.configure(state=DISABLED)
        E_BROWNIE.set("0")

    if (var7.get() == 1):
        txtBLACKFOREST_CAKE.configure(state=NORMAL)
    elif var7.get() == 0:
        txtBLACKFOREST_CAKE.configure(state=DISABLED)
        E_BLACKFOREST_CAKE.set("0")

    if (var8.get() == 1):
        txtREDVELVET_CAKE.configure(state=NORMAL)
    elif var8.get() == 0:
        txtREDVELVET_CAKE.configure(state=DISABLED)
        E_REDVELVET_CAKE.set("0")

    if (var9.get() == 1):
        txtRAINBOW_CAKE.configure(state=NORMAL)
    elif var9.get() == 0:
        txtRAINBOW_CAKE.configure(state=DISABLED)
        E_RAINBOW_CAKE.set("0")

    if (var10.get() == 1):
        txtBUTTERSCOTCH_CAKE.configure(state=NORMAL)
    elif var10.get() == 0:
        txtBUTTERSCOTCH_CAKE.configure(state=DISABLED)
        E_BUTTERSCOTCH_CAKE.set("0")


# ----------------for TOTAL button--------------------------
def COI():
    ITEM1 = float(E_COCO_COLA.get())
    ITEM2 = float(E_PEPSI.get())
    ITEM3 = float(E_FANTA.get())
    ITEM4 = float(E_SPRITE.get())
    ITEM5 = float(E_APPY.get())

    ITEM6 = float(E_BROWNIE.get())
    ITEM7 = float(E_BLACKFOREST_CAKE.get())
    ITEM8 = float(E_REDVELVET_CAKE.get())
    ITEM9 = float(E_RAINBOW_CAKE.get())
    ITEM10 = float(E_BUTTERSCOTCH_CAKE.get())

    POD = (ITEM1 * 30) + (ITEM2 * 30) + (ITEM3 * 30) + (ITEM4 * 30) + (ITEM5 * 30)

    POC = (ITEM6 * 50) + (ITEM7 * 60) + (ITEM9 * 70) + (ITEM9 * 80) + (ITEM10 * 90)

    DP = "Rs.", str('%.2f' % (POD))
    CP = "Rs.", str('%.2f' % (POC))
    COC.set(CP)
    COD.set(DP)
    AA = "Rs.", str('%.2f' % (10))
    SC.set(AA)

    STOI = "Rs.", str('%.2f' % (POD + POC + 10))
    ST.set(STOI)

    Tax = "Rs.", str('%.2f' % ((POD + POC) * (0.05)))
    PT.set(Tax)
    EX = (POD + POC) * (0.05)
    TOC = "Rs.", str('%.2f' % (POD + POC + 10 + EX))
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
    txtReceipt.insert(END, 'COCO_COLA: \t\t' + E_COCO_COLA.get() + "\n")
    txtReceipt.insert(END, 'PEPSI: \t\t' + E_PEPSI.get() + "\n")
    txtReceipt.insert(END, 'FANTA: \t\t' + E_FANTA.get() + "\n")
    txtReceipt.insert(END, 'SPRITE: \t\t' + E_SPRITE.get() + "\n")
    txtReceipt.insert(END, 'APPY: \t\t' + E_APPY.get() + "\n")
    txtReceipt.insert(END, 'BROWNIE: \t\t' + E_BROWNIE.get() + "\n")
    txtReceipt.insert(END, 'BLACKFOREST_CAKE: \t\t' + E_BLACKFOREST_CAKE.get() + "\n")
    txtReceipt.insert(END, 'REDVELVET_CAKE: \t\t' + E_REDVELVET_CAKE.get() + "\n")
    txtReceipt.insert(END, 'RAINBOW_CAKE: \t\t' + E_RAINBOW_CAKE.get() + "\n")
    txtReceipt.insert(END, 'Cost Of Drinks:\t\t' + COD.get() + "\n" + 'Tax Paid:\t' + PT.get() + "\n")
    txtReceipt.insert(END, 'Cost Of Cakes:\t\t' + COC.get() + "\n" + 'Sub Total:\t' + ST.get() + "\n")
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

E_COCO_COLA = StringVar()
E_PEPSI = StringVar()
E_FANTA = StringVar()
E_SPRITE = StringVar()
E_APPY = StringVar()

E_BROWNIE = StringVar()
E_BLACKFOREST_CAKE = StringVar()
E_REDVELVET_CAKE = StringVar()
E_RAINBOW_CAKE = StringVar()
E_BUTTERSCOTCH_CAKE = StringVar()

E_COCO_COLA.set("0")
E_PEPSI.set("0")
E_FANTA.set("0")
E_SPRITE.set("0")
E_APPY.set("0")

E_BROWNIE.set("0")
E_BLACKFOREST_CAKE.set("0")
E_REDVELVET_CAKE.set("0")
E_RAINBOW_CAKE.set("0")
E_BUTTERSCOTCH_CAKE.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))

# -----------------------DRINKS-------------------------
COCO_COLA = Checkbutton(f1aa, text="COCO-COLA \t\t", variable=var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                        command=chkbutton_value).grid(row=0, sticky=W)

PEPSI = Checkbutton(f1aa, text="PEPSI \t\t", variable=var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkbutton_value).grid(row=1, sticky=W)

FANTA = Checkbutton(f1aa, text="FANTA \t\t", variable=var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                    command=chkbutton_value).grid(row=2, sticky=W)

SPRITE = Checkbutton(f1aa, text="SPRITE \t\t", variable=var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                     command=chkbutton_value).grid(row=3, sticky=W)

APPY = Checkbutton(f1aa, text="APPY \t\t", variable=var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                   command=chkbutton_value).grid(row=4, sticky=W)

# ------------------------Cakes-----------------------------
BROWNIE = Checkbutton(f1ab, text="BROWNIE \t", variable=var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'),
                      command=chkbutton_value).grid(row=0, sticky=W)

BLACKFOREST_CAKE = Checkbutton(f1ab, text="BLACKFOREST CAKE \t", variable=var7, onvalue=1, offvalue=0,
                               font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=1, sticky=W)

REDVELVET_CAKE = Checkbutton(f1ab, text="REDVELVET CAKE \t", variable=var8, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=2, sticky=W)

RAINBOW_CAKE = Checkbutton(f1ab, text="RAINBOW CAKE \t", variable=var9, onvalue=1, offvalue=0,
                           font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)

BUTTERSCOTCH_CAKE = Checkbutton(f1ab, text="BUTTERSCOTCH CAKE \t", variable=var10, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=4, sticky=W)

# ---------------------Widgets for drinks--------------------
txtCOCO_COLA = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_COCO_COLA,
                     state=DISABLED)
txtCOCO_COLA.grid(row=0, column=1)
txtPEPSI = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_PEPSI, state=DISABLED)
txtPEPSI.grid(row=1, column=1)
txtFANTA = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_FANTA, state=DISABLED)
txtFANTA.grid(row=2, column=1)
txtSPRITE = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_SPRITE,
                  state=DISABLED)
txtSPRITE.grid(row=3, column=1)
txtAPPY = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_APPY, state=DISABLED)
txtAPPY.grid(row=4, column=1)

# --------------------------Widgets for cakes----------------
txtBROWNIE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_BROWNIE,
                   state=DISABLED)
txtBROWNIE.grid(row=0, column=1)
txtBLACKFOREST_CAKE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                            textvariable=E_BLACKFOREST_CAKE, state=DISABLED)
txtBLACKFOREST_CAKE.grid(row=1, column=1)
txtREDVELVET_CAKE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                          textvariable=E_REDVELVET_CAKE, state=DISABLED)
txtREDVELVET_CAKE.grid(row=2, column=1)
txtRAINBOW_CAKE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_RAINBOW_CAKE,
                        state=DISABLED)
txtRAINBOW_CAKE.grid(row=3, column=1)
txtBUTTERSCOTCH_CAKE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_BUTTERSCOTCH_CAKE, state=DISABLED)
txtBUTTERSCOTCH_CAKE.grid(row=4, column=1)

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
lb1PT = Label(f2ab, font=('arial', 12, 'bold'), text="TAX", bd=8, anchor='w')
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