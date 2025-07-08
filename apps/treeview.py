from tkinter import *
from tkinter import ttk

windows = Tk()
windows.title("PyNerd App")

tree = ttk.Treeview(windows, selectmode="browse", column=("column1", "column2", "column3", "column4"), show="headings")

tree.column("column1", width=200, minwidth=50, stretch=NO)
tree.heading("#1", text="Nome")

tree.column("column2", width=100, minwidth=50, stretch=NO)
tree.heading("#2", text="Idade")

tree.column("column3", width=300, minwidth=50, stretch=NO)
tree.heading("#3", text="Endereço")

tree.column("column4", width=75, minwidth=50, stretch=NO)
tree.heading("#4", text="ID")
tree.grid(row=0, column=0)

elements = ["Joaquin", "13", "Cidade Baixa", 1]

for i in range(0,4):
    tree.insert("", END, values=elements, tags="1")

windows.mainloop()
