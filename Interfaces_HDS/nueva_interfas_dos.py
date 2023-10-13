# inportamos tkinter
from tkinter import*

# instanciar la clase Tk
ventana=Tk()

# creo mis dos widget de orden inferior con la clase Frame()
# instanciamos mi primer widget
widget_uno=Frame()
# usar metodo pára montar el frame
widget_uno.grid(row="0",column="0")
widget_uno.config(width="100",height="100")
widget_uno.config(bg="blue")
# el metodo grid recibe dos parametros el numero de las columna ey el numero de la fila donde quiero ubicar mi widget

# creacion del segundo widget
widget_dos=Frame()
widget_dos.grid(row="2",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="green")

# usar la funcion loop para que la ventana permanesca abierta
ventana.mainloop()