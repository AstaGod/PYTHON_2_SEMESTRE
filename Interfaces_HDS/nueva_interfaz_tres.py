# inportamos tkinter
from tkinter import*

# instanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")

# creo mis dos widget de orden inferior con la clase Frame()
windget_uno1=Frame()
windget_uno1.grid(row=0,column=0)
windget_uno1.config(width=400,height=50)
# windget_uno1.config(bg="red")
 
# creacion de etiquetas
etiqueta=Label(ventana,text="Ingresa tu nombre")
etiqueta.grid(row=1,column=0)

# creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)
# usar la funcion loop para que la ventana permanesca abierta
ventana.mainloop()