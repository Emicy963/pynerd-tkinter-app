from tkinter import *

def mostrar():
    armazem_label["text"] = "Button Click"

windows = Tk()
windows.title("PyNerd App")
windows.geometry("700x400")
windows.resizable(False, False)

Button(windows, text="Click Here", bg="black", fg="white", height=10, width=20, command=mostrar).grid(row=0, column=0)

armazem_label = Label(windows, text="No Click")
armazem_label.grid(row=1, column=0)

windows.mainloop()
