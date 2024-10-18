from tkinter import *
from tkinter import ttk
import random
import string

root = Tk()
root.title("gera senha 3000")

def gerar_senha():
    try:
        tamanho = int(entrada.get())
        if tamanho<8:
            resultado.config(text="A senha deve ter no mínimo 8 caracteres")
        else:
            caracteres = string.ascii_letters + string.digits + "!@#$%*"
            senha = ''.join(random.choice(caracteres) for i in range(tamanho))
            resultado.config(text=(senha))
    except ValueError:
        resultado.config(text="Valor inválido")

mainframe = ttk.Frame(root, padding="6 6 6 6")
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

texto = ttk.Label(mainframe, text="Digite o tamanho da senha (Mínimo 8 digitos)")

entrada = ttk.Entry(mainframe, width=16)

botao = ttk.Button(mainframe, text="Gerar Senha", command=gerar_senha)

resultado = ttk.Label(mainframe, text="")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()