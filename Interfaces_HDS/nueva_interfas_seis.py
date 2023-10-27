# importar la librerisa
from tkinter import *
# intanciamos nuestra clase Tk()
ventana=Tk() # clase para crear una ventana
ventana.title("clase radiobutton") # haciendo uso del metodo title para el titulo de mi ventana
ventana.geometry("400x300") # haciendo uso del metodo geometry para asignarle un tamaño de ventana

# instanciar mi clase Label
etiqueta=Label(ventana,text="radio button") # clase para crear una etiqueta
# indicar la parte de mi ventana que deseo que se muestre
# puedo usar los metodos grid o pack
etiqueta.config(fg="#EB6828",font=5)
etiqueta.pack()

info=IntVar()
def mostrar_radio():
    # respuesta = "eres masculino" if info.get()==1 else "eres femenino"
    # etiquetaRespuesta=Label(ventana,text=respuesta)
    # etiquetaRespuesta.pack()
    if info.get()==1:
        mensaje=Label(ventana,text=" eres masculino")      
        mensaje.pack()
        print(info.get())
    elif info.get()==0:
        mensaje=Label(ventana,text=" eres femenino")
        mensaje.pack()
        print(info.get())
# instanciar la clase Radiobutton
radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radioFemenino.pack()

# instanciar la clase button
boton=Button(ventana,text="Enviar",command=mostrar_radio)
boton.pack()
# lloamar al metyodo de Tk que me permite tener persistencia al mostrarla la ventana
ventana.mainloop()