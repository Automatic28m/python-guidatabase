from tkinter import *
import subprocess
import pymysql
from tkinter import messagebox

win = Tk()
win.title("Login")
win.geometry("350x180")
win.option_add("*font", "Bahnschrift 11")

# Container
fm1 = Frame(win)
fm1.place(y=20)


# Grid or Table
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

    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    # Label Username, Password
    add_grid(Label(fm1, text="Username: ", width=15, anchor=E), 0, 0)
    add_grid(Label(fm1, text="Password: ", width=15, anchor=E), 1, 0)

    # TextBox txtUsername, txtPassword
    txtUsername = Entry(fm1, textvariable=stvUsername, width=20)
    add_grid(txtUsername, 0, 1)
    txtPassword = Entry(fm1, textvariable=stvPassword, width=20)
    add_grid(txtPassword, 1, 1)

    add_grid(Button(fm1, text="Login", width=15, command=lambda: login()), 2, 1)

    lblLogin = Label(fm1, text=">>ลงทะเบียน ? คลิก", font="Bahnschrift 13", fg="red")
    lblLogin.bind("<Button-1>", lambda e: open_regis())
    add_grid(lblLogin, 2, 0)

    # Search Data (Select)
    def login():
        username = stvUsername.get()
        password = stvPassword.get()

        query = (
            f"SELECT firstname, lastname FROM `user` WHERE username='{username}'"
            f" AND password='{password}';"
        )

        cursor.execute(query)
        rows = cursor.fetchall()

        if (
            not username or not password
        ):  # ตรวจสอบให้แน่ใจว่า Username และ Password ไม่เป็นค่าว่าง
            messagebox.showerror("Login Info", "กรุณากรอกข้อมูลให้ครบ")
        elif rows:
            # Assuming there is only one row returned
            user_data = rows[0]
            messagebox.showinfo(
                "ยินดีต้อนรับเข้าสู่ระบบ",
                "Login Success คุณ" + user_data[0] + " " + user_data[1],
            )
        else:
            # Clear the variables if no results found
            messagebox.showerror("การแจ้งเตือน", "กรุณาตรวจสอบ Username และ Password")
            stvUsername.set("")
            stvPassword.set("")

    def open_regis():
        win.destroy()
        subprocess.Popen(["python", "ManageUser/register.py"])

    win.mainloop()
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")


finally:
    cursor.close()
    connection.close()
