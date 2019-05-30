## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 


import tkinter as tk
from tkinter import ttk



class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Formulario")

        self.treeview = ttk.Treeview(self)
        item = self.treeview.insert("", tk.END, text="Rosario")
        self.treeview.insert(item, tk.END, text="2000")
        item = self.treeview.insert("", tk.END, text="Roldan")
        self.treeview.insert(item, tk.END, text="2134")
        item = self.treeview.insert("", tk.END, text="Funes")
        self.treeview.insert(item, tk.END, text="2132")
        item = self.treeview.insert("", tk.END, text="San Lorenzo")
        self.treeview.insert(item, tk.END, text="2200")
        item = self.treeview.insert("", tk.END, text="Villa Gobernador Gálvez")
        self.treeview.insert(item, tk.END, text="2124")
        self.treeview.pack()

        self.pack()


main_window = tk.Tk()
app = Application(main_window) #instancio

#Inicio alta
def form_alta():
    otra_ventana = tk.Toplevel(main_window) #creo una nueva ventana
    main_window.iconify() #minimizo la principal
    txt_ciudad = tk.StringVar() #instancio las variables para los entry
    txt_CP = tk.StringVar()
    label = tk.Label(otra_ventana, text="Ciudad: ")
    label2 = tk.Label(otra_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))

    #tuve que separar la definicion del grid porque si no no asiganba la variable.
    Ciudad = tk.Entry(otra_ventana,textvariable=txt_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(otra_ventana,textvariable=txt_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(otra_ventana, text="Agregar")
    btn_alta.grid(column=3, row=2, padx=(50,50), pady=(10,10))
    def alta(event):
        print(Ciudad.get())
        item = app.treeview.insert("", tk.END, text=Ciudad.get())
        app.treeview.insert(item, tk.END, text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", alta)

btn_frm_alta = tk.Button(main_window, text="Dar de alta una Ciudad", command=form_alta)
btn_frm_alta.pack()
#Fin alta

#Inicio Baja
def baja():
    curItem = app.treeview.focus() #trae el elemento que está seleccionado
    app.treeview.delete(curItem)
btn_baja = tk.Button(main_window, text="Baja", command=baja)
btn_baja.pack()
#Fin Baja

#Inicio Modificacion
def form_modificacion():
    otra_ventana = tk.Toplevel(main_window) #creo una nueva ventana
    main_window.iconify() #minimizo la principal
    elem = app.treeview.focus()
    elem_child = app.treeview.focus()
    print (app.treeview.item(elem))
    txt_ciudad = tk.StringVar(otra_ventana, value=app.treeview.item(elem)['text']) #instancio las variables para los entry

    txt_CP = tk.StringVar(otra_ventana, value=app.treeview.item(elem)['text'])
    label = tk.Label(otra_ventana, text="Ciudad: ")
    label2 = tk.Label(otra_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))

    #tuve que separar la definicion del grid porque si no no asiganba la variable.
    Ciudad = tk.Entry(otra_ventana,textvariable=txt_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(otra_ventana,textvariable=txt_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(otra_ventana, text="Modificar")
    btn_alta.grid(column=3, row=2, padx=(50,50), pady=(10,10))
    def alta(event):
        print(Ciudad.get())
        item = app.treeview.insert("", tk.END, text=Ciudad.get())
        app.treeview.insert(item, tk.END, text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", alta)

btn_frm_alta = tk.Button(main_window, text="Modificar", command=form_modificacion)
btn_frm_alta.pack()
#Fin Modificacion
app.mainloop()
