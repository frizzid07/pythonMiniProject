from tkinter import *

root = Tk()
k=1
for i in range(5):
    table =Frame(root)
    for j in range(3):
        Button(table,fg="springgreen",bg="dark slate gray",activebackground="springgreen",font=("Helvetica", 14),activeforeground="goldenrod",padx=70,pady=70,text="Table %d" % (k)).pack()
        k=k+1
    table.grid(row=0, column=i)
root.title("Tables")
root.mainloop()
