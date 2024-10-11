from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Milhas para KM")

def calculate():
    try:
        miles_value = float(miles.get())
        kilometers_value = miles_value * 1.609
        kilometers.set(f"{kilometers_value:}")
    except ValueError:
        kilometers.set("Entrada Inválida")
    
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

miles = StringVar()
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W,E))

kilometers= StringVar()
ttk.Label(mainframe, textvariable=kilometers).grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Quilômetros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

miles_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
