from time import sleep
from tkinter import *
from tkinter import messagebox
from file.File import File
from utils.Creator import Creator
from core.atualizador import Atualizador

class Application:
    
    def __init__(self, master=None) -> None:
        self.master = master
        self.core = Atualizador()
        self.mainConteiner = Creator.createConteiner(parent=master, geometry="Pack")
        messagebox.showinfo("Lembrete", "Certifique-se que o banco de dados da CHG está atualizado antes realizar o processo.")
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
        self.dbStatus = self.m3Success = Creator.createDBStatusLabel(parent=self.master, text="Tentando se conectar com as bases de dados...", success=True)
        self.connectionButton.destroy()
        root.update_idletasks()
        sleep(3)
        
        if self.core.startM3():
            self.dbStatus['text'] = "Banco de dados M3 conectado"
            root.update_idletasks()
            sleep(2)
            if self.core.startCHG():
                self.dbStatus['text'] = "Banco de dados CHG conectado"
                root.update_idletasks()
                sleep(2)
                if not self.fazerBackupBaseDeDadosM3():
                    messagebox.showwarning("Aviso", "Não foi possível realizar o backup da base de dados. Você pode continuar o processo, mas é recomendado realizar o backup manualmente.")
                self.updateButton = Creator.createButton(
                    parent=self.master,
                    command=self.atualizar,
                    text="Iniciar",
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
    
    def fazerBackupBaseDeDadosM3(self):
        f = File()
        if f.loadFile():
            self.dbStatus['text'] = "Fazendo backup da base de dados..."
            root.update_idletasks()
            sleep(3)
            if f.makeBackup():
                self.dbStatus['text'] = "Backup realizado, sistema pronto para iniciar o processo."
                return True
        else:
            self.BkpLabel.destroy()
            return False

    def atualizar(self):
        self.dbStatus.destroy()
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

        self.core.atualizar(tkList=productsList, root=root)

root = Tk(className="Atualizador CHG")
root.resizable(False, False)
root.configure(bg='white')
root.geometry("700x500")
Application(root)
root.mainloop()