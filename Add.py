from tkinter import *

def addGUIPanel():
   m1 = PanedWindow()
   m1.pack(fill=BOTH, expand=1)
   left = Label(m1, text="left pane")
   m1.add(left)
   return

