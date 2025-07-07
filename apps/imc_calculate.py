from tkinter import *

def calculate():
    peso_get = float(peso.get())
    altura_get = float(altura.get())

    imc = peso_get / (altura_get * altura_get)

    reply["text"] = f"Seu IMC é: {imc:.2f}"

windows = Tk()
windows.title("PyNerd App")
windows.geometry("300x300")
windows.resizable(False, False)

Label(windows, text="Calcula o seu IMC").grid(row=0, column=0, columnspan=2)

Label(windows,text="Insira o seu peso:").grid(row=1, column=0)

peso = Entry(windows)
peso.grid(row=1, column=1)

Label(windows,text="Insira A sua altura:").grid(row=2, column=0)

altura = Entry(windows)
altura.grid(row=2, column=1)

Button(windows, text="Calcular", command=calculate).grid(row=3, column=0)

reply = Label(windows, text="resultado")
reply.grid(row=3, column=1)

windows.mainloop()
