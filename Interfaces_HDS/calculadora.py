from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

# class Funciones y Operaciones:
widget1 = Entry(ventana)
widget1.grid(row=0, column=0, columnspan=4, sticky=W + E)
i=0

def iportar_numero(n):
    global i
    widget1.insert(i,n)
    i+=1

def operaciones(operador):
    global i
    longitud_operador=len(operador)
    widget1.insert(i,operador)
    i+=longitud_operador

def limpiar():
    widget1.delete(0,END)

def calcular():
    calcular_entrada = widget1.get()
    try:
        resultado = eval(calcular_entrada)  
        limpiar()
        widget1.insert(0, resultado)
    except Exception as e:
        limpiar()
        widget1.insert(0, "ERROR")

boton1=Button(ventana,text="1",command=lambda:iportar_numero(1)).grid(row=1,column=0,sticky=W+E)
boton2=Button(ventana,text="2",command=lambda:iportar_numero(2)).grid(row=1,column=1,sticky=W+E)
boton3=Button(ventana,text="3",command=lambda:iportar_numero(3)).grid(row=1,column=2,sticky=W+E)
boton4=Button(ventana,text="4",command=lambda:iportar_numero(4)).grid(row=2,column=0,sticky=W+E)
boton5=Button(ventana,text="5",command=lambda:iportar_numero(5)).grid(row=2,column=1,sticky=W+E)
boton6=Button(ventana,text="6",command=lambda:iportar_numero(6)).grid(row=2,column=2,sticky=W+E)
boton7=Button(ventana,text="7",command=lambda:iportar_numero(7)).grid(row=3,column=0,sticky=W+E)
boton8=Button(ventana,text="8",command=lambda:iportar_numero(8)).grid(row=3,column=1,sticky=W+E)
boton9=Button(ventana,text="9",command=lambda:iportar_numero(9)).grid(row=3,column=2,sticky=W+E)
boton10=Button(ventana,text="0",command=lambda:iportar_numero(0)).grid(row=4,column=0,sticky=W+E)
boton11=Button(ventana,text="=",command=lambda:calcular()).grid(row=4,column=1,columnspan=2,sticky=W+E)
boton12=Button(ventana,text="+",command=lambda:operaciones("+")).grid(row=1,column=3,sticky=W+E)
boton13=Button(ventana,text="-",command=lambda:operaciones("-")).grid(row=2,column=3,sticky=W+E)
boton14=Button(ventana,text="x",command=lambda:operaciones("*")).grid(row=3,column=3,sticky=W+E)
boton15=Button(ventana,text="/",command=lambda:operaciones("/")).grid(row=4,column=3,sticky=W+E)
boton16=Button(ventana,text="Clear",command=lambda:limpiar()).grid(row=5,column=0,columnspan=4,sticky=W+E)

ventana.mainloop()