import tkinter as tk
import math as math

calculo = ""

def add_calculo(valor):
    global calculo
    calculo += str(valor)
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def raiz_quadrada():
    global calculo
    calculo = str(round(math.sqrt(float(calculo)), 3))
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
tela.title("Romario")
tela.geometry("450x410")

texto = tk.Text(tela, height=2, width=25, font = ("Arial", 24))
texto.grid(columnspan=6)

btn_1 = tk.Button(tela, text="1", command=lambda: add_calculo(1), width=5, font=("Arial", 24))
btn_1.grid(row=3, column=1)
 
btn_2 = tk.Button(tela, text="2", command=lambda: add_calculo(2), width=5, font=("Arial", 24))
btn_2.grid(row=3, column=2)
 
btn_3 = tk.Button(tela, text="3", command=lambda: add_calculo(3), width=5, font=("Arial", 24))
btn_3.grid(row=3, column=3)

btn_4 = tk.Button(tela, text="4", command=lambda: add_calculo(4), width=5, font=("Arial", 24))
btn_4.grid(row=4, column=1)
 
btn_5 = tk.Button(tela, text="5", command=lambda: add_calculo(5), width=5, font=("Arial", 24))
btn_5.grid(row=4, column=2)
 
btn_6 = tk.Button(tela, text="6", command=lambda: add_calculo(6), width=5, font=("Arial", 24))
btn_6.grid(row=4, column=3)
 
btn_7 = tk.Button(tela, text="7", command=lambda: add_calculo(7), width=5, font=("Arial", 24))
btn_7.grid(row=5, column=1)
 
btn_8 = tk.Button(tela, text="8", command=lambda: add_calculo(8), width=5, font=("Arial", 24))
btn_8.grid(row=5, column=2)
 
btn_9 = tk.Button(tela, text="9", command=lambda: add_calculo(9), width=5, font=("Arial", 24))
btn_9.grid(row=5, column=3)
 
btn_0 = tk.Button(tela, text="0", command=lambda: add_calculo(0), width=11, font=("Arial", 24))
btn_0.grid(row=6, column=1, columnspan=2)
 
btn_add = tk.Button(tela, text="+", command=lambda: add_calculo('+'), width=5, height=5, font=("Arial", 24))
btn_add.grid(row=4, rowspan=3, column=4)

btn_min = tk.Button(tela, text="-", command=lambda: add_calculo("-"), width=5, font=("Arial", 24))
btn_min.grid(row=3, column=4)
 
btn_div = tk.Button(tela, text="/", command=lambda: add_calculo("/"), width=5, font=("Arial", 24))
btn_div.grid(row=2, column=3)

btn_multi = tk.Button(tela, text="*", command=lambda: add_calculo("*"), width=5, font=("Arial", 24))
btn_multi.grid(row=2, column=4)
 
btn_raiz = tk.Button(tela, text="RaQ", command=lambda: raiz_quadrada(), width=5, font=("Arial", 24))
btn_raiz.grid(row=2, column=2)
 
btn_result = tk.Button(tela, text="=", command=lambda: calcular_resultado(), width=5, font=("Arial", 24))
btn_result.grid(row=6, column=3)
 
btn_limpar = tk.Button(tela, text="C", command=lambda: limpar(), width=5, font=("Arial", 24))
btn_limpar.grid(row=2, column=1)
 

tela.mainloop()