from tkinter import *

windows = Tk()
windows.title("PyNerd App")
windows.geometry("700x400")
windows.resizable(False, False)

Entry(windows, bg="black", fg="orange", show="*").grid(row=0, column=0)

windows.mainloop()
