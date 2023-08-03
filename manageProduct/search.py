from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import pymysql

win = Tk()
win.title("Search Product")
win.geometry("570x250")
win.option_add("*font", "Bahnschrift 11")

# Container
fm1 = Frame(win)
fm1.place(x=58, y=20)


# Connect Database(phpMyAdmin)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "myshop",
}


# Grid (Table)
def add_grid(widget, r, c):
    widget.grid(row=r, column=c, padx=5, pady=10)


try:
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # variable (ตัวแปร)
    productID = StringVar()
    productName = StringVar()
    typeID = StringVar()
    unitPrice = StringVar()

    # Label ProductID, ProductName, ProductType, ProductPrice
    add_grid(Label(fm1, text="ProductID : ", width=15, anchor=E), 0, 0)
    add_grid(Label(fm1, text="ProductName : ", width=15, anchor=E), 1, 0)
    add_grid(Label(fm1, text="ProductType : ", width=15, anchor=E), 2, 0)
    add_grid(Label(fm1, text="ProductPrice : ", width=15, anchor=E), 3, 0)

    # TextBox
    txtProductID = Entry(fm1, textvariable=productID, width=20)
    add_grid(txtProductID, 0, 1)
    txtProductName = Entry(fm1, textvariable=productName, width=20, state="disabled")
    add_grid(txtProductName, 1, 1)
    txtProductPrice = Entry(fm1, textvariable=typeID, width=20, state="disabled")
    add_grid(txtProductPrice, 2, 1)
    txtProductType = Entry(fm1, textvariable=unitPrice, width=20, state="disabled")
    add_grid(txtProductType, 3, 1)

    add_grid(Button(fm1, text="Search", width=15, command=lambda: search()), 0, 2)
    add_grid(Button(fm1, text="Back", width=15, command=lambda: open_main()), 1, 2)

    # Search Data (Select)
    def search():
        product_id = productID.get()
        query = f"select tbproduct.productName , tbproduct.unitPrice , tbtype.typeName from tbproduct inner join tbtype ON tbproduct.typeID= tbtype.typeID WHERE `productID`={product_id}"

        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            # Assuming there is only one row returned
            product_data = rows[0]
            productName.set(product_data[0])
            unitPrice.set(product_data[1])
            typeID.set(product_data[2])
        else:
            # Clear the variables if no results found
            messagebox.showerror("Error", "ไม่พบข้อมูล")
            productName.set("")
            typeID.set("")
            unitPrice.set("")

    # Home Page(Main)
    def open_main():
        win.destroy()
        subprocess.Popen(["python", "manageProduct\home.py"])

    win.mainloop()

except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")


finally:
    cursor.close()
    connection.close()
