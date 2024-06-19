import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manager")
        self.build()

    def build(self):
        button = tk.Button(self, text="Click me!", command= self.hello)
        button.pack()

    def hello(self):
        print("Hello, World!")



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
