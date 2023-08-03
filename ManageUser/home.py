from tkinter import *
import subprocess


class Gui:
    def __init__(self):
        self.win = Tk()
        self.win.title("ManageUser")
        self.win.resizable(0, 0)
        self.win.geometry("350x250")

        self.fm1 = Frame(self.win)
        self.fm1.place(x=45, y=55)

        self.fm = Frame(self.win, bg="#FFEDB5")
        self.fm.pack()
        self.lbl1 = Label(
            self.fm,
            text="สมาชิกผู้จัดทำ",
            bg="#FFEDB5",
            width=250,
            font="Bahnschrift 18",
        )
        self.lbl1.pack(pady=10)

        self.add_grid(
            Label(self.fm1, text="1. ", font="Bahnschrift 12"),
            1,
            0,
        )

        self.add_grid(
            Label(
                self.fm1,
                text="นายณัฏฐากร เกษประดิษฐ",
                font="Bahnschrift 15",
            ),
            1,
            1,
        )

        self.add_grid(
            Label(self.fm1, text="2. ", font="Bahnschrift 12"),
            2,
            0,
        )

        self.add_grid(
            Label(
                self.fm1,
                text="นายภูริทร์ ทัศคร",
                font="Bahnschrift 15",
            ),
            2,
            1,
        )

        self.add_grid(
            Label(self.fm1, text="3. ", font="Bahnschrift 12"),
            3,
            0,
        )

        self.add_grid(
            Label(
                self.fm1,
                text="นายพัลลภ บุญเหลือ",
                font="Bahnschrift 15",
            ),
            3,
            1,
        )

        lblLogin = Label(
            self.fm1, text="คลิก...เพื่อเข้าสู่ระบบ", font="Bahnschrift 16", fg="red"
        )
        lblLogin.bind("<Button-1>", lambda e: self.open_login())
        self.add_grid(lblLogin, 4, 1)

        self.win.mainloop()

    def add_grid(self, widget, r, c):
        widget.grid(row=r, column=c, padx=10, pady=5)

    # สร้าง Label เรียกใช้ฟังก์ชัน open_regis

    def open_login(self):
        self.win.destroy()
        subprocess.Popen(["python", "ManageUser/login.py"])


if __name__ == "__main__":
    Gui()
