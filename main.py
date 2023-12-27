import tkinter as tk

calculo = ""

def add_calculo(valor):
    global calculo
    calculo += str(valor)
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def calcular_resultado():
    global calculo
    try:
        calculo = str(eval(calculo))
        texto.delete(1.0, "end")   
        texto.insert(1.0, calculo)
    except:
        limpar()
        texto.insert(1.0, "Erro")


def limpar():
    global calculo
    calculo = ""
    texto.delete(1.0, "end")

tela = tk.Tk()
tela.geometry("300x200")

texto = tk.Text(tela, height=2, width=16, font = ("Arial", 24))
texto.grid(columnspan=5)

btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_2 = tk.Button(tela, text="2", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_2.grid(row=2, column=2)
 
btn_3 = tk.Button(tela, text="3", command=lambda: add_calculo(3), width=5, font=("Arial", 24))
btn_3.grid(row=2, column=3)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 
btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=2, column=1)
 

tela.mainloop()