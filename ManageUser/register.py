from tkinter import *
import subprocess
import pymysql
from tkinter import messagebox, ttk

win = Tk()
win.title("Register")
win.geometry("500x400")
win.option_add("*font", "Bahnschrift 11")

fm1 = Frame(win)
fm1.place(y=20)


def add_grid(widget, r, c):
    widget.grid(row=r, column=c, padx=5, pady=10)


# Connect Database(phpMyAdmin)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mydatabase",
}

try:
    # Variable(ตัวแปรไว้สำหรับเก็บค่า)
    stvUsername = StringVar()
    stvPassword = StringVar()
    result_user = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    selected_option = StringVar(win)
    selected_option.set("นาย")

    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    add_grid(Label(fm1, text="Username:", width=15, anchor=E), 0, 0)
    add_grid(Label(fm1, text="Password:", width=15, anchor=E), 1, 0)
    add_grid(
        Label(fm1, text="คำนำหน้าชื่อ: ", width=15, font="Bahnschrift 14", anchor=E),
        2,
        0,
    )
    add_grid(Label(fm1, text="ชื่อ: ", width=15, font="Bahnschrift 14", anchor=E), 3, 0)
    add_grid(
        Label(fm1, text="นามสกุล:", width=15, font="Bahnschrift 14", anchor=E), 4, 0
    )
    add_grid(Label(fm1, text="E-mail:", width=15, anchor=E), 5, 0)

    txtUsername = Entry(fm1, textvariable=stvUsername, width=20)
    add_grid(txtUsername, 0, 1)
    txtPassword = Entry(fm1, state="readonly", width=20)
    add_grid(txtPassword, 1, 1)

    # ตัวแปรเก็บค่าการเลือกใน combobox
    selected_option = StringVar(win)
    selected_option.set("นาย")

    # ชุดคำสั่งสร้างตัวเลือก combobox
    combo = ttk.Combobox(
        fm1, values=["โปรดเลือก", "นาย", "นาง", "นางสาว"], state="readonly", width=17
    )
    combo.current(0)
    add_grid(combo, 2, 1)

    # ทดสอบการคลิกปุ่ม result เพื่อทดสอบผลลัพธ์จากการเลือกแสดงผลใน Label
    add_grid(Button(fm1, text="result", command=lambda: getResult()), 6, 2)
    result_combo = StringVar(value=selected_option.get())
    add_grid(
        Label(
            fm1, textvariable=result_combo, font="Bahnschrift 15", fg="red", anchor=E
        ),
        5,
        2,
    )

    # Set ค่าให้ตัวแปร result_combo จากการเลือกcombobox
    def getResult():
        result_combo.set(combo.get())

    txtName = Entry(fm1, width=20)
    add_grid(txtName, 3, 1)
    txtLastname = Entry(fm1, width=20)
    add_grid(txtLastname, 4, 1)
    txtEmail = Entry(fm1, width=20)
    add_grid(txtEmail, 5, 1)

    # Button
    add_grid(Button(fm1, text="Check", width=10, command=lambda: Check()), 0, 2)

    btnRegistration = Button(
        fm1, text="ลงทะเบียน", font="Bahnschrift 14", state="disable", width=15
    )
    add_grid(btnRegistration, 6, 1)

    # Search Data (Select)
    def Check():
        if txtUsername.get() != "":
            username = stvUsername.get()
            query = f"SELECT username FROM `user` WHERE username='{username}';"

            cursor.execute(query)
            rows = cursor.fetchall()

            if len(rows) == 0:
                btnRegistration.config(state="normal")
                txtPassword.config(state="normal")
            else:
                messagebox.showerror("การแจ้งเตือน", "Username นี้ มีผู้ใช้แล้ว")
        else:
            messagebox.showerror("การแจ้งเตือน", "กรุณากรอก Username")

    win.mainloop()

except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")


finally:
    cursor.close()
    connection.close()
