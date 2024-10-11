from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora de IMC 3000")

def calcular():
    try:
        peso_value = float(peso.get())
        altura_value = float(altura.get())
        #permite calcular tanto em metros quanto em centimetros (eu fiquei 1h30 tentando fazer isso)
        if altura_value > 3:
            altura_value /= 100
        if altura_value == 0:
            imc.set("Altura Inválida")
        else:
            imc_value = peso_value / (altura_value * altura_value)
            print(imc_value)
            imc.set(f"{imc_value:.2f}")
    except ValueError:
        imc.set("Entrada Inválida")

mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#eu tentei fazer aparecer "Altura" meio transparente na caixinha de texto mas não consegui
altura = StringVar()
altura_entry = ttk.Entry(mainframe, width=10, textvariable=altura)
altura_entry.grid(column=1, row=1, sticky=(W,E))

peso = StringVar()
peso_entry = ttk.Entry(mainframe, width=10, textvariable=peso)
peso_entry.grid(column=1, row=3, sticky=(W,E))

imc = StringVar()
ttk.Label(mainframe, textvariable=imc).grid(column=2, row=3, sticky=(W,E))

ttk.Button(mainframe, text="Calcular", command=calcular).grid(column=3, row=3, sticky=(W))

#deixa bonitinho
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()