from tkinter import *
import subprocess


class Gui:
    def __init__(self):
        self.win = Tk()
        self.win.title("Admin")
        self.win.resizable(0, 0)
        self.win.geometry("300x250")

        self.fm1 = Frame(self.win)
        self.fm1.place(x=45, y=55)

        self.fm = Frame(self.win, bg="#FFEDB5")
        self.fm.pack()
        self.lbl1 = Label(
            self.fm,
            text="Admin / Manager",
            bg="#FFEDB5",
            width=250,
            font="Bahnschrift 15",
        )
        self.lbl1.pack(pady=10)

        self.add_grid(
            Button(
                self.fm1,
                text="Search",
                font="Bahnschrift 12",
                width=20,
                command=lambda: self.open_search(),
            ),
            1,
            1,
        )

        self.add_grid(
            Button(
                self.fm1,
                text="Add",
                font="Bahnschrift 12",
                width=20,
                command=lambda: self.open_add(),
            ),
            2,
            1,
        )

        self.add_grid(
            Button(
                self.fm1,
                text="Update",
                font="Bahnschrift 12",
                width=20,
                command=lambda: self.open_update(),
            ),
            3,
            1,
        )

        self.add_grid(
            Button(
                self.fm1,
                text="Delete",
                font="Bahnschrift 12",
                width=20,
                command=lambda: self.open_delete(),
            ),
            4,
            1,
        )
        self.win.mainloop()

    def add_grid(self, widget, r, c):
        widget.grid(row=r, column=c, padx=10, pady=5)

    def open_search(self):
        self.win.withdraw()
        subprocess.Popen(["python", "manageProduct\search.py"])

    def open_add(self):
        pass

    def open_update(self):
        pass

    def open_delete(self):
        pass


if __name__ == "__main__":
    Gui()
