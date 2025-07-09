from tkinter import *

windows = Tk()
windows.title("PyNerd App")
windows.geometry("500x500")

frame = Frame(windows, width=300, height=300, bg="white").grid(row=0, column=0)
Label(frame, text="Test Frame").grid(row=0, column=0)

windows.mainloop()
