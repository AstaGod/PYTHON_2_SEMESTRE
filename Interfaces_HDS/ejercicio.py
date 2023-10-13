from tkinter import*
ventana=Tk()

Widget_uno=Frame()
Widget_uno.grid(row="0",column="0")
Widget_uno.config(width="100",height="100")
Widget_uno.config(bg="blue")

Widget_dos=Frame()
Widget_dos.grid(row="0",column="1")
Widget_dos.config(width="100",height="100")
Widget_dos.config(bg="green")

Widget_tres=Frame()
Widget_tres.grid(row="1",column="0")
Widget_tres.config(width="200",height="100")
Widget_tres.config(bg="purple")

Widget_cuatro=Frame()
Widget_cuatro.grid(row="2",column="0")
Widget_cuatro.config(width="200",height="100")
Widget_cuatro.config(bg="yellow")

Widget_cinco=Frame()
Widget_cinco.grid(row="3",column="0")
Widget_cinco.config(width="50",height="100")
Widget_cinco.config(bg="blue")

Widget_seis=Frame()
Widget_seis.grid(row="3",column="1")
Widget_seis.config(width="50",height="100")
Widget_seis.config(bg="green")

Widget_siete=Frame()
Widget_siete.grid(row="3",column="2")
Widget_siete.config(width="50",height="100")
Widget_siete.config(bg="red")

Widget_ocho=Frame()
Widget_ocho.grid(row="3",column="3")
Widget_ocho.config(width="50",height="100")
Widget_ocho.config(bg="blue")

ventana.mainloop()