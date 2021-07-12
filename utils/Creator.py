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
    def createScrollBar(parent):
        scrollBar = Scrollbar(parent)
        scrollBar.pack(side=RIGHT, fill=Y)
        return scrollBar

    @staticmethod
    def createListBox(parent, options):
        listbox = Listbox(parent, yscrollcommand=options['yscrollcommand'], bg=options['bg'], font=options['font'], width=options['width'], height=options['height'])
        listbox.pack(side=LEFT, fill=BOTH)
        return listbox

    @staticmethod
    def createConteiner(parent, geometry):
        conteiner = Frame(parent)
        Creator.setGeometry(conteiner, geometry, pady=30)    
        return conteiner
    
    @staticmethod
    def createButton(parent, command, text, options):
        button = Button(parent, command=command, text=text, font=options['font'], bg=options['bg'], fg=options['fg'], bd=options['bd'])
        Creator.setGeometry(button, options['geometry'], pady=30)
        return button

    @staticmethod
    def createLabel(parent, text, options):
        label = Label(parent, text=text, font=options['font'], bg=options['bg'], fg=options['fg'])
        Creator.setGeometry(label, options['geometry'])
        return label

    @staticmethod
    def createDBStatusLabel(parent, text, success):
        options = {
            'geometry': "Pack",
            'font': ("Verdana", "10"),
            'bg': 'white',
            'fg': 'dark green' if success else 'red3'
        }
        return Creator.createLabel(parent=parent, text=text, options=options)