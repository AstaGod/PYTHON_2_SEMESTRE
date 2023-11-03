from tkinter import*
root=Tk()
root.geometry("300x300")

frameL=LabelFrame(root,text="cuadrito",padx=20,pady=20)
frameL.config(width=200,height=200)
frameL.pack(pady=15)

Variable=1
texto=Entry(frameL,width=20)
texto.insert(0,str(Variable)+" mundo")
texto.pack()

root.mainloop()