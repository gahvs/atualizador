from tkinter import *
from utils.Creator import Creator

class Application:
    
    def __init__(self, master=None) -> None:
        
        self.mainConteiner = Creator.createConteiner(parent=master, geometry="Pack")
        self.mainTitle = Creator.createTitle(
            parent=master,
            text="Atualizador CHG",
            options={
                'geometry':"Pack",
                'font': ("Verdana", "20"),
                'bg': 'white',
                'fg': 'salmon'
            }
        )
        self.mainButton = Creator.createButton(
            parent=master,
            text="Atualizar",
            options={
                'geometry':"Pack",
                'font': ("Verdana", "15"),
                'bg': 'white',
                'fg': 'salmon'
            }
        )

        
root = Tk(className="Atualizador CHG")
root.geometry("500x500")
root.configure(bg='white')
Application(root)
root.mainloop()