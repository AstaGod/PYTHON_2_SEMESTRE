from tkinter import*
ventana=Tk()
ventana.geometry("250x300")

ventana.title("ventana suma")

def captura_dato():                                 #.get sirve para capturar datos
    text=text_nombre.get()                          #Label sirve para crear una ventana
    mensaje=Label(ventana,text=f"hola, {text}")     #Entry es para crear un cuadro 
    mensaje.pack()                                  #Button para crear boton

etiqueta=Label(ventana,text="introduce tu nombre")
etiqueta.pack()
text_nombre=Entry(ventana)
text_nombre.config(bg="red",fg="yellow")
text_nombre.pack()

boton_capturar=Button(ventana,text="enviar",command=captura_dato)
boton_capturar.pack()

ventana.mainloop()