from tkinter import *

root = Tk()

mylabel = Label( root, text = 'I am a label Widget')
mybutton = Button(root, text = 'I am a button')
mylabel.pack()
mybutton.pack()

root.mainloop()