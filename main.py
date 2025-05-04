from tkinter import *

windows = Tk()
windows.title("PyNerd App")
windows.geometry("700x400")
windows.resizable(False, False)

Label(windows, text="E aí, PyNerd!", bg="black", fg="white", padx=30, pady=30).grid(row=0, column=0)

windows.mainloop()
