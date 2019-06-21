from tkinter import *
import Add 
root = Tk()

def donothing():
  #root.add_command(Add.addGUIPanel,command=None)
  #label = root.Label(window, text = "Hello World!").pack()
 
  
menuBar = Menu(root)
filemenu= Menu(menuBar,tearoff=0)
filemenu.add_command(label="New",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
menuBar.add_cascade(label="File",menu=filemenu)



root.config(menu=menuBar)
root.mainloop()
