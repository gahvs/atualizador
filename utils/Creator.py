from tkinter import *

class Creator:

    @staticmethod
    def setGeometry(element, geometry, padx=None, pady=None):
        if geometry ==  "Place": 
            element.place(padx=padx, pady=pady)
        elif geometry == "Grid": 
            element.grid(padx=padx, pady=pady)
        elif geometry == "Pack": 
            element.pack(padx=padx, pady=pady)

    @staticmethod
    def createConteiner(parent, geometry):
        conteiner = Frame(parent)
        Creator.setGeometry(conteiner, geometry, pady=30)    
        return conteiner
    
    @staticmethod
    def createButton(parent, text, options):
        button = Button(parent, text=text, font=options['font'], bg=options['bg'], fg=options['fg'])
        Creator.setGeometry(button, options['geometry'], pady=30)
        return button

    @staticmethod
    def createTitle(parent, text, options):
        title = Label(parent, text=text, font=options['font'], bg=options['bg'], fg=options['fg'])
        Creator.setGeometry(title, options['geometry'])
        return title