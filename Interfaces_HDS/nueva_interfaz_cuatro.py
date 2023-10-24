from tkinter import*
ventana=Tk()
ventana.geometry("500x400")

heade=Frame()
heade.grid(row=0,column=1,columnspan=4)
heade.config(width=500,height=15,bg="red")

aside_left=Frame()
aside_left.grid(row=1,column=0,rowspan=7)
aside_left.config(width=15,height=385,bg="red") 

ventana.mainloop()