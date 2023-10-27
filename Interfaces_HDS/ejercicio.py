# from tkinter import*
# ventana=Tk()

# Widget_uno=Frame()
# Widget_uno.grid(row="0",column="0")
# Widget_uno.config(width="100",height="100")
# Widget_uno.config(bg="blue")

# Widget_dos=Frame()
# Widget_dos.grid(row="0",column="1")
# Widget_dos.config(width="100",height="100")
# Widget_dos.config(bg="green")

# Widget_tres=Frame()
# Widget_tres.grid(row="1",column="0")
# Widget_tres.config(width="200",height="100")
# Widget_tres.config(bg="purple")

# Widget_cuatro=Frame()
# Widget_cuatro.grid(row="2",column="0")
# Widget_cuatro.config(width="200",height="100")
# Widget_cuatro.config(bg="yellow")

# Widget_cinco=Frame()
# Widget_cinco.grid(row="3",column="0")
# Widget_cinco.config(width="50",height="100")
# Widget_cinco.config(bg="blue")

# Widget_seis=Frame()
# Widget_seis.grid(row="3",column="1")
# Widget_seis.config(width="50",height="100")
# Widget_seis.config(bg="green")

# Widget_siete=Frame()
# Widget_siete.grid(row="3",column="2")
# Widget_siete.config(width="50",height="100")
# Widget_siete.config(bg="red")

# Widget_ocho=Frame()
# Widget_ocho.grid(row="3",column="3")
# Widget_ocho.config(width="50",height="100")
# Widget_ocho.config(bg="blue")

# ventana.mainloop()


# EJERCICIO 2
# from tkinter import*
# ventana=Tk()

# Widget_uno=Frame()
# Widget_uno.grid(row="0",column="0")
# Widget_uno.config(width="100",height="100")
# Widget_uno.config(bg="red")

# Widget_dos=Frame()
# Widget_dos.grid(row="0",column="1")
# Widget_dos.config(width="100",height="100")
# Widget_dos.config(bg="green")

# Widget_tres=Frame()
# Widget_tres.grid(row="1",column="0")
# Widget_tres.config(width="100",height="100")
# Widget_tres.config(bg="purple")

# Widget_cuatro=Frame()
# Widget_cuatro.grid(row="1",column="1")
# Widget_cuatro.config(width="100",height="100")
# Widget_cuatro.config(bg="yellow")

# Widget_cinco=Frame()
# Widget_cinco.grid(row="2",column="0")
# Widget_cinco.config(width="100",height="100")
# Widget_cinco.config(bg="blue")

# Widget_seis=Frame()
# Widget_seis.grid(row="2",column="1")
# Widget_seis.config(width="100",height="100")
# Widget_seis.config(bg="green")

# ventana.mainloop()

# EJERCICIO 3
# from tkinter import*
# ventana=Tk()

# Widget_uno=Frame()
# Widget_uno.grid(row="0",rowspan="2",column="0")
# Widget_uno.config(width="100",height="200")
# Widget_uno.config(bg="red")

# Widget_dos=Frame()
# Widget_dos.grid(row="0",column="1")
# Widget_dos.config(width="100",height="100")
# Widget_dos.config(bg="green")

# Widget_cuatro=Frame()
# Widget_cuatro.grid(row="1",column="1")
# Widget_cuatro.config(width="100",height="100")
# Widget_cuatro.config(bg="yellow")

# Widget_cinco=Frame()
# Widget_cinco.grid(row="2",column="0",columnspan="2")
# Widget_cinco.config(width="200",height="100")
# Widget_cinco.config(bg="blue")

# ventana.mainloop()

# EJERCICIO 4
# from tkinter import*

# ventana=Tk()
# ventana.geometry("260x355")

# invisible0=Label(ventana,text="")
# invisible0.grid(row=0,column=1)

# etiqueta_uno=Label(ventana,text="Nombres y Apellidos")
# etiqueta_uno.grid(row=1,column=1)

# invisible1=Label(ventana,text="")
# invisible1.grid(row=2,column=1)

# etiqueta_dos=Label(ventana,text="DNI")
# etiqueta_dos.grid(row=3,column=1)

# invisible2=Label(ventana,text="")
# invisible2.grid(row=4,column=1)

# etiqueta_tres=Label(ventana,text="Celular")
# etiqueta_tres.grid(row=5,column=1)

# invisible3=Label(ventana,text="")
# invisible3.grid(row=6,column=1)

# cuadro_texto=Entry()
# cuadro_texto.grid(row=1,column=2)

# cuadro_texto=Entry()
# cuadro_texto.grid(row=3,column=2)

# cuadro_texto=Entry()
# cuadro_texto.grid(row=5,column=2)

# widget_uno=Frame()
# widget_uno.grid(row=7,column=1,columnspan=2)
# widget_uno.config(width=240,height=200)
# widget_uno.config(bg="red")

# widget_invisible=Frame()
# widget_invisible.grid(rowspan=7,column=0)
# widget_invisible.config(width=10,height=350)

# ventana.mainloop()

#Ejercicio 5

# from tkinter import*
# ventana=Tk()
# ventana.geometry("250x300")

# ventana.title("ventana edad")

# def captura_edad():                                 
#     text=int(text_edad.get())  
#     if text >=18:
#         mensaje=Label(ventana,text="Tas listo pa chambear :)")      
#         mensaje.pack()   
#     else:
#         mensaje=Label(ventana,text="eres wawa")      
#         mensaje.pack()                                   
# etiqueta=Label(ventana,text="introduzca tu edad ")
# etiqueta.pack()
# text_edad=Entry(ventana)
# text_edad.config(bg="red",fg="yellow")
# text_edad.pack()

# boton_capturar=Button(ventana,text="enviar",command=captura_edad)
# boton_capturar.pack()

# ventana.mainloop()

# EJERCICIO 6

# from tkinter import*
# ventana=Tk()
# ventana.geometry("250x300")
# ventana.title("Papu misterioso")

# def comprobar_datos():
#     text1=text_usuario.get()
#     text2=int(text_contra.get())
#     if text1 == usuario and text2==contra:
#         mensaje=Label(ventana,text="Vienvenido csmr :)")      
#         mensaje.pack()
#     else:
#         mensaje=Label(ventana,text="quien eres csmr")      
#         mensaje.pack()

# usuario="Asta"
# contra=71439102

# etiqueta1=Label(ventana,text="Introdusca su nombre de usuario")
# etiqueta1.pack()

# text_usuario=Entry(ventana)
# text_usuario.config(bg="red",fg="white")
# text_usuario.pack()

# etiqueta2=Label(ventana,text="Ingrese su contra")
# etiqueta2.pack()

# text_contra=Entry(ventana)
# text_contra.config(bg="red",fg="white",show="*")
# text_contra.pack()
# boton_capturar=Button(ventana,text="Comprovar",command=comprobar_datos)
# boton_capturar.pack()

# ventana.mainloop()

# EJERCICIO 7
