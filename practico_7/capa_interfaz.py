
from practico_05.ejercicio_01 import Socio
from practico_06 import capa_negocio
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox


negocio = capa_negocio.NegocioSocio()

class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("ABM Socios")

        self.treeview = ttk.Treeview(self)
        self.treeview["columns"]=("Nombre","Apellido","DNI")
        self.treeview.column("#0", width=270, minwidth=270, stretch=tk.NO)
        self.treeview.column("Nombre", width=150, minwidth=150, stretch=tk.NO)
        self.treeview.column("Apellido", width=400, minwidth=200, stretch=tk.NO)
        self.treeview.column("DNI", width=80, minwidth=50, stretch=tk.NO)

        self.treeview.heading("#0",text="ID Socio",anchor=tk.W)
        self.treeview.heading("Nombre", text="Nombre",anchor=tk.W)
        self.treeview.heading("Apellido", text="Apellido",anchor=tk.W)
        self.treeview.heading("DNI", text="DNI",anchor=tk.W)

        socios_all = negocio.todos()
        for socio in socios_all:
            self.treeview.insert("",tk.END,iid = None   , text=socio.id_socio, values=(socio.nombre,socio.apellido,socio.dni))
        self.treeview.grid(columnspan= 4,row=1)
        self.grid(columnspan= 3,row=1)

#Inicio del formulario de alta
def form_alta():
    frm_alta = tk.Toplevel(main_window) #creo una nueva ventana

    txt_nombre = tk.StringVar() #instancio las variables para los entry
    txt_apellido = tk.StringVar()
    txt_dni = tk.StringVar()

    label = tk.Label(frm_alta, text="Nombre: ")
    label2 = tk.Label(frm_alta, text="Apellido: ")
    label3 = tk.Label(frm_alta, text="DNI: ")

    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))
    label3.grid(column=3, row=1, padx=(40,40), pady=(10,5))

    nombre = ttk.Entry(frm_alta,textvariable=txt_nombre)
    nombre.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    apellido = ttk.Entry(frm_alta,textvariable=txt_apellido)
    apellido.grid(column=2, row=2, padx=(5,5), pady=(10,5))
    dni = ttk.Entry(frm_alta,textvariable=txt_dni)
    dni.grid(column=3, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(frm_alta, text="Agregar")
    btn_alta.grid(column=4, row=2, padx=(20,20), pady=(10,10))
    btn_cancel = tk.Button(frm_alta, text="Cancelar")
    btn_cancel.grid(column=5, row=2, padx=(20,20), pady=(10,10))



    def alta(event):
        socio = Socio(dni = txt_dni.get(),nombre = txt_nombre.get(),apellido = txt_apellido.get())
        error=False

        try:
            negocio.alta(socio)
        except Exception as err:
            error=True
            mbox.showerror('Error', str(err), parent=frm_alta)

        if error==False:
            app.treeview.insert("",tk.END,id = socio.id_socio   , text=socio.id_socio, values=(socio.nombre,socio.apellido,socio.dni))
            main_window.deiconify()
            frm_alta.destroy()


    def close_window(event):
        frm_alta.destroy()
    btn_cancel.bind("<Button-1>", close_window)
    btn_alta.bind("<Button-1>", alta)




#Fin alta

#Inicio Baja
def baja():
    item_tv = app.treeview.focus() #identificador del item en el treeView
    curItem = app.treeview.item(item_tv)['text'] #El id del elemento para borrarlo
    negocio.baja(curItem)
    app.treeview.delete(item_tv)

#Fin Baja

#Inicio Modificacion
def form_modificacion():
    frm_modificacion = tk.Toplevel(main_window) #creo una nueva ventana
    #main_window.iconify() #minimizo la principal
    elem = app.treeview.focus()
    curItem = app.treeview.item(elem)
    txt_nombre = tk.StringVar(frm_modificacion, value=curItem['values'][0]) #instancio las variables para los entry
    txt_apellido = tk.StringVar(frm_modificacion, value=curItem['values'][1])
    txt_dni = tk.StringVar(frm_modificacion, value=curItem['values'][2])
    label = tk.Label(frm_modificacion, text="Nombre: ")
    label2 = tk.Label(frm_modificacion, text="Apellido: ")
    label3 = tk.Label(frm_modificacion, text="DNI: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))
    label3.grid(column=3, row=1, padx=(40,40), pady=(10,5))

    #tuve que separar la definicion del grid porque si no no asiganba la variable.
    nombre = tk.Entry(frm_modificacion,textvariable=txt_nombre)
    nombre.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    apellido = tk.Entry(frm_modificacion,textvariable=txt_apellido)
    apellido.grid(column=2, row=2, padx=(5,5), pady=(10,5))
    dni = tk.Entry(frm_modificacion,textvariable=txt_dni)
    dni.grid(column=3, row=2, padx=(5,5), pady=(10,5))
    btn_cancel = tk.Button(frm_modificacion, text="Cancelar")
    btn_cancel.grid(column=5, row=2, padx=(20,20), pady=(10,10))

    btn_mod = tk.Button(frm_modificacion, text="Modificación")
    btn_mod.grid(column=4, row=2, padx=(20,20), pady=(10,10))

    def modificacion(event):
        socio = Socio(id_socio = curItem['text'],dni = txt_dni.get(),nombre = txt_nombre.get(),apellido = txt_apellido.get())
        error=False

        try:
            negocio.modificacion(socio)
        except Exception as err:
            error=True
            mbox.showerror('Error', str(err), parent=frm_modificacion)



        if error==False:
            app.treeview.item(elem,text=curItem['text'],values=(txt_nombre.get(),txt_apellido.get(),txt_dni.get())) #.update(Ciudad.get())
            frm_modificacion.destroy()
            main_window.deiconify()


    def close_window(event):
        frm_modificacion.destroy()
    btn_cancel.bind("<Button-1>", close_window)
    btn_mod.bind("<Button-1>", modificacion)

#Fin Modificacion


main_window = tk.Tk()

#Botones de la ventana principal
btn_frm_alta = tk.Button(main_window, text="Alta", command=form_alta)
btn_frm_alta.grid(column=0, row=2, padx=(20,20), pady=(10,10))

btn_frm_mod = tk.Button(main_window, text="Modificar", command=form_modificacion)
btn_frm_mod.grid(column=2, row=2, padx=(20,20), pady=(10,10))

btn_baja = tk.Button(main_window, text="Baja", command=baja)
btn_baja.grid(column=1, row=2, padx=(20,20), pady=(10,10))

app = Application(main_window)
app.mainloop()
