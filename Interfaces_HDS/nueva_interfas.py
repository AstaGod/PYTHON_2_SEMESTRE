#1. import tkinter -> libreria para la creacion de interfaces grafica
# import tkinter as tk #-> una forma de usar
# root=tk.Tk()

from tkinter import*
# la libreria tkinter tiene tre grande clases para la creacion de interfaces
# Tk()  -> el mas usado
# Tkk()
# Tcl()
#2, instanciar Tk() como generador de interfaz grafica
nueva_ventana=Tk()

#3. frame es tambien una clase Frame() para crear un frame tengo que primero instaciarlo
menu_principal=Frame()
# montamos o inicializamos el frmae
menu_principal.pack()
# haciendo uso del metodo config le damos un tamano
menu_principal.config(width="200",height="200")
# haciendo uso del metodo config le adignamos un color
menu_principal.config(bg="red")

menu_principal2=Frame()
# montamos o inicializamos el frmae
menu_principal2.pack()
# haciendo uso del metodo config le damos un tamano
menu_principal2.config(width="200",height="200")
# haciendo uso del metodo config le adignamos un color
menu_principal2.config(bg="blue")

# metodo de Tk() que mantien la ejecucion del programa en un bucle
nueva_ventana.mainloop()