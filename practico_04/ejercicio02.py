## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 


from tkinter import *
calculadora=Tk()
calculadora.title("Calculadora")
calculadora.geometry("392x600")


def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) #ESTA PARTE SIRVE PARA VISUALIZAR LA OPERACION EN LA PANTALLA

def operacion():
    global operador
    try:
        opera=str(eval(operador))#SIRVE PARA REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
    except:
        opera=("ERROR")
    input_text.set(opera)#MUESTRA EL RESULTADO


color_boton = "grey"
ancho_boton=7
alto_boton=2
input_text=StringVar()
operador=""
Boton0=Button(calculadora,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=360)
Boton1=Button(calculadora,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=17,y=300)
Boton2=Button(calculadora,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=107,y=300)
Boton3=Button(calculadora,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=197,y=300)
Boton4=Button(calculadora,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Boton5=Button(calculadora,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Boton6=Button(calculadora,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Boton7=Button(calculadora,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=17,y=180)
Boton8=Button(calculadora,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=107,y=180)
Boton9=Button(calculadora,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=197,y=180)
BotonSuma=Button(calculadora,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=287,y=180)
BotonResta=Button(calculadora,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=287,y=240)
BotonMulti=Button(calculadora,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=287,y=300)
BotonDiv=Button(calculadora,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
BotonResul=Button(calculadora,text="=",bg=color_boton,width=ancho_boton*2+6,height=alto_boton,command=operacion).place(x=107,y=360)

Pantalla=Entry(calculadora,font=('arial',25,'bold'),textvariable=input_text,justify="right").pack(side="top",ipady=20,pady=30)


calculadora.mainloop()
