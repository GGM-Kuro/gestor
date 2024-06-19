import tkinter as tk
from tkinter import ttk

import database as db


class CenterWidgetMixin(tk.Tk):
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)
        self.geometry(f"{w}x{h}+{x}+{y}")


class MainWindow(CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Manager")
        self.build()

    def build(self):
        frame = tk.Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview["columns"] = ("DNI", "NAME", "LASTNAME")

        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("DNI", anchor=tk.CENTER)
        treeview.column("NAME", anchor=tk.CENTER)
        treeview.column("LASTNAME", anchor=tk.CENTER)

        treeview.heading("DNI", text="DNI", anchor=tk.CENTER)
        treeview.heading("NAME", text="NAME", anchor=tk.CENTER)
        treeview.heading("LASTNAME", text="LASTNAME", anchor=tk.CENTER)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        treeview["yscrollcommand"] = scrollbar.set

        for client in db.Clients.list:
            treeview.insert(
                parent="",
                index="end",
                iid=client.dni,
                values=(client.dni, client.name, client.last_name),
            )

        treeview.pack()

        frame = tk.Frame(self)
        frame.pack(pady=20)


        tk.Button(frame, text="Create", command=tk.NONE).grid(row=0, column=0)
        tk.Button(frame, text="Modify", command=tk.NONE).grid(row=0, column=1)
        tk.Button(frame, text="Delete", command=tk.NONE).grid(row=0, column=2)

        self.treeview = treeview


    def hello(self):
        print("Hello, World!")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
