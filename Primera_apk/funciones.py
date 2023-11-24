from tkinter import *
from tkinter.messagebox import *

def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellido=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellido,celular))
    showinfo(title="Nuevo",message="Nuevo contacto agregado")
    f_limpiar(ventana)

def f_eliminar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()
    print(item_seleccionado)
    if item_seleccionado:
        ventana.tabla_datos.delete(item_seleccionado)
        showwarning(title="ELIMINAR",message="Registro elimnado")
        f_limpiar(ventana)
    else:
        print("Selecciona una fila para eliminar.")

def f_actualizar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()
    if item_seleccionado:
        # Obtén los nuevos datos de las cajas de texto o de donde los estés ingresando
        nuevo_nombre = ventana.nombre_texto.get()
        nuevo_apellido = ventana.apellidos_texto.get()
        nuevo_celular = ventana.celular_texto.get()

        # Actualiza los valores en la tabla
        ventana.tabla_datos.item(item_seleccionado, text=nuevo_nombre, values=(nuevo_apellido, nuevo_celular))
        f_limpiar(ventana)
    else:
        print("Selecciona una fila para actualizar.")

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askokcancel(title="ACTUALIZAR",message="Desea actualizar los datos")
    if mensaje == True:
        print(captura_datos["text"],captura_datos["Values"][0],captura_datos["Values"][1])
    else:
        showinfo(title="ACTUALIZAR",message="Ningun registro seleccionado para actualizar")