from tkinter import *
from utils.Creator import Creator
from core.atualizador import Atualizador

class Application:
    
    def __init__(self, master=None) -> None:
        self.master = master
        self.core = Atualizador()
        self.mainConteiner = Creator.createConteiner(parent=master, geometry="Pack")
        self.mainTitle = Creator.createLabel(
            parent=master,
            text="Atualizador CHG",
            options={
                'geometry':"Pack",
                'font': ("Verdana", "20"),
                'bg': 'white',
                'fg': 'orange red'
            }
        )
        self.mainTitle['pady'] = 30
        self.connectionButton = Creator.createButton(
            parent=master,
            command=self.conectarBasesDeDados,
            text="Conectar bases de dados",
            options={
                'geometry':"Pack",
                'font': ("Calibri", "12"),
                'bg': 'white',
                'fg': 'orange red',
                'bd': 1,
            }
        )

    def conectarBasesDeDados(self):
        self.connectionButton.destroy()
        
        if self.core.startM3():
            self.m3Success = Creator.createDBStatusLabel(parent=self.master, text="Banco de dados M3 conectado", success=True)
            if self.core.startCHG():
                self.chgSuccess = Creator.createDBStatusLabel(parent=self.master, text="Banco de dados CHG conectado", success=True)
                self.updateButton = Creator.createButton(
                    parent=self.master,
                    command=self.atualizar,
                    text="Atualizar",
                    options = {
                        'geometry':"Pack",
                        'font': ("Calibri", "12"),
                        'bg': 'white',
                        'fg': 'orange red',
                        'bd': 1,
                    }
                )
            else :
                self.chgFail = Creator.createDBStatusLabel(parent=self.master, text="Falha ao se comunicar com o banco de dados CHG", success=False)    
        else:
            self.m3Fail = Creator.createDBStatusLabel(parent=self.master, text="Falha ao se comunicar com o banco de dados M3", success=False)
            
    def atualizar(self):
        self.m3Success.destroy()
        self.chgSuccess.destroy()
        self.updateButton.destroy()
        self.scrollBar = Creator.createScrollBar(self.master)
        productsList = Creator.createListBox(parent=self.master, options={
            'geometry': "Pack",
            'yscrollcommand': self.scrollBar.set,
            'bg': 'gray99',
            'font': ("Calibri", "12"),
            'width': 100,
            'height': 150,
            'bd': 1,
        })
        self.scrollBar.config(command=productsList.yview)

        self.core.atualizar(tkList=productsList)
        
root = Tk(className="Atualizador CHG")
root.resizable(False, False)
root.geometry("500x500")
root.configure(bg='white')
Application(root)
root.mainloop()