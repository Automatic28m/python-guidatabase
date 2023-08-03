from tkinter import *

win = Tk()
win.title("Insert Product")
win.geometry("500x300")
win.option_add("*font", "Bahnschrift 11")

var = IntVar()
var.set("1")  # กำหนดตัวเลือกเริ่มต้น
typeRadio = StringVar()
typeRadio.set("1")

fm1 = Frame(win)
fm1.place(x=35, y=20)


def add_grid(widget, r, c):
    widget.grid(row=r, column=c, padx=5, pady=10)


add_grid(Label(fm1, text="ProductID : ", width=15, anchor=E), 0, 0)
add_grid(Label(fm1, text="ProductName : ", width=15, anchor=E), 1, 0)
add_grid(Label(fm1, text="ProductPrice : ", width=15, anchor=E), 2, 0)
add_grid(Label(fm1, text="ProductType : ", width=15, anchor=E), 3, 0)


txtProductID = Entry(fm1, width=20)
add_grid(txtProductID, 0, 1)
txtProductName = Entry(fm1, width=20)
add_grid(txtProductName, 1, 1)
txtProductPrice = Entry(fm1, width=20)
add_grid(txtProductPrice, 2, 1)

add_grid(
    Radiobutton(
        fm1, text="Beverage", variable=var, value=1, command=lambda: getvalue()
    ),
    3,  # row
    1,  # column
)
add_grid(
    Radiobutton(
        fm1, text="Bakery", variable=var, value=2, width=15, command=lambda: getvalue()
    ),
    3,  # row
    2,  # column
)


add_grid(Label(fm1, textvariable=typeRadio), 5, 2)


# getค่าจากradiobutton
def getvalue():
    typeRadio.set(var.get())


add_grid(Button(fm1, text="Add", width=15, command=lambda: open_add()), 4, 1)


def open_add():
    pass


win.mainloop()
