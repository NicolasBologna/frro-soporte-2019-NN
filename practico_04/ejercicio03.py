## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

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
app = Application(main_window)
app.mainloop()
