from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('hello\nda')

l = Label(root, textvariable = var)
l.pack()

for i in range(6):
    sleep(1) # Need this to slow the changes down
    var.set('goodbye\nda' if i%2 else 'hello\nda')
    root.update_idletasks()