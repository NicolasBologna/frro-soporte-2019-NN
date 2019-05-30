## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
 
import tkinter as tk

calculadora = tk.Tk()
calculadora.title('Calculadora')


def pide_cerrar():
    calculadora.destroy()
    calculadora.quit()
calculadora.protocol("WM_DELETE_WINDOW", pide_cerrar)


label = tk.Label(calculadora, text="Primer Operando: ")
label2 = tk.Label(calculadora, text="Segundo Operando: ")
label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))
evar1 = tk.DoubleVar()
evar1.set('')
evar2 = tk.DoubleVar()
evar2.set('')
res = tk.DoubleVar()
entry1 = tk.Entry(calculadora,textvariable = evar1)
entry2 = tk.Entry(calculadora,textvariable = evar2)
entry1.grid(column=1, row=2)
entry2.grid(column=2, row=2)

btn_mas = tk.Button(calculadora, text="+")
def sumar(event):
    try:
        res.set(evar1.get() + evar2.get())
        evar1.set('')
        evar2.set('')
        print(res.get())
        lbl_res['text'] = res.get() #permite cambiar atributos mientras está corriendo
    except:
         lbl_res['text'] = 'Error'
btn_mas.bind("<Button-1>", sumar)

btn_menos = tk.Button(calculadora, text="-")
def restar(event):
    try:
        res.set(evar1.get() - evar2.get())
        evar1.set('')
        evar2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_menos.bind("<Button-1>", restar)


btn_por = tk.Button(calculadora, text="*")
def multiplicar(event):
    try:
        res.set(evar1.get() * evar2.get())
        evar1.set('')
        evar2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_por.bind("<Button-1>", multiplicar)


btn_div = tk.Button(calculadora, text="/")
def dividir(event):
    try:
        res.set(evar1.get() / evar2.get())
        evar1.set('')
        evar2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_div.bind("<Button-1>", dividir)

lbl_res = tk.Label(calculadora, text=res.get())

btn_mas.grid(column=3, row=2, padx=(5,5), pady=(10,5))
btn_menos.grid(column=4, row=2, padx=(5,5), pady=(10,5))
btn_por.grid(column=5, row=2, padx=(5,5), pady=(10,5))
btn_div.grid(column=6, row=2, padx=(5,5), pady=(10,5))
lbl_res.grid(column=3, row=3, padx=(5,5), pady=(10,5))


calculadora.mainloop()


