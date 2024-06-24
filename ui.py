import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
import helpers

import database as db


class CenterWidgetMixin:
    def center(self):
        self.update()  # pyright: ignore
        w = self.winfo_width()  # pyright: ignore
        h = self.winfo_height()  # pyright: ignore
        ws = self.winfo_screenwidth()  # pyright: ignore
        hs = self.winfo_screenheight()  # pyright: ignore
        x = int(ws / 2 - w / 2)  # pyright: ignore
        y = int(hs / 2 - h / 2)  # pyright: ignore
        self.geometry(f"{w}x{h}+{x}+{y}")  # pyright: ignore


class CreateClientWindow(tk.Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create Client")
        self.build()

    def build(self):
        frame = tk.Frame(self)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="DNI (2 int and 1 char)").grid(row=0, column=0)
        tk.Label(frame, text="Name (from 2 to 30 chars)").grid(row=0, column=1)
        tk.Label(frame, text="Last Name (from 2 to 30 chars)").grid(row=0, column=2)

        dni = tk.Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        name = tk.Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        last_name = tk.Entry(frame)
        last_name.grid(row=1, column=2)
        last_name.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = tk.Frame(self)
        frame.pack(pady=10)

        create = tk.Button(frame, text="Create", command=self.create_client)
        create.config(state=tk.DISABLED)
        create.grid(row=0, column=0)

        tk.Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [False, False, False]
        self.create = create
        self.dni = dni
        self.name = name
        self.last_name = last_name

    def create_client(self):
        self.master.treeview.insert(
            parent="",
            index="end",
            iid=self.dni.get(),
            values=(self.dni.get(), self.name.get(), self.last_name.get()))
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = (
            helpers.validate_dni(value, db.Clients.list)
            if index == 0
            else (value.isalpha() and len(value) >= 2 and len(value) <= 30)
        )
        event.widget.configure({"bg": "green" if valid else "red"})

        # NOTE: change button state based on validations
        self.validations[index] = valid
        self.create.config(
            state=tk.NORMAL if self.validations == [True, True, True] else tk.DISABLED
        )

class EditClientWindow(tk.Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modify Client")
        self.build()

    def build(self):
        frame = tk.Frame(self)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="DNI (NOT editable)").grid(row=0, column=0)
        tk.Label(frame, text="Name (from 2 to 30 chars)").grid(row=0, column=1)
        tk.Label(frame, text="Last Name (from 2 to 30 chars)").grid(row=0, column=2)

        dni = tk.Entry(frame)
        name = tk.Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        last_name = tk.Entry(frame)
        last_name.grid(row=1, column=2)
        last_name.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        client = self.master.treeview.focus()
        fields = self.master.treeview.item(client, "values")
        dni.insert(0, fields[0])
        dni.config(state=tk.DISABLED)
        name.insert(0, fields[1])
        last_name.insert(0, fields[2])

        frame = tk.Frame(self)
        frame.pack(pady=10)

        modify = tk.Button(frame, text="Update", command=self.update_client)
        modify.grid(row=0, column=0)

        tk.Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [True, True]
        self.modify = modify
        self.dni = dni
        self.name = name
        self.last_name = last_name

    def update_client(self):
        client = self.master.treeview.focus()
        self.master.treeview.item(client, values=(self.dni.get(),self.name.get(),self.last_name.get()))
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = (
            (value.isalpha() and len(value) >= 2 and len(value) <= 30)
        )
        event.widget.configure({"bg": "green" if valid else "red"})

        # NOTE: change button state based on validations
        self.validations[index] = valid
        self.modify.config(
            state=tk.NORMAL if self.validations == [True, True] else tk.DISABLED
        )


class MainWindow(tk.Tk, CenterWidgetMixin):
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

        tk.Button(frame, text="Create", command=self.create).grid(row=0, column=0)
        tk.Button(frame, text="Modify", command=self.edit).grid(row=0, column=1)
        tk.Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def delete(self):
        client = self.treeview.focus()
        if client:
            campos = self.treeview.item(client, "values")
            confirm = askokcancel(
                title="confirm delete",
                message=f"delete {campos[1]} {campos[2]}?",
                icon=WARNING,
            )
            if confirm:
                self.treeview.delete(client)

    def create(self):
        CreateClientWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
