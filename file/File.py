import os

class File:

    def __init__(self) -> None:
        self.__file = None
        self.__bkpFileName = "bkp.bat"
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __getFBBinPath(self) -> str or None:
        try:
            conf = open("conf", 'r')
            return [_ for _ in conf][0]
        except FileNotFoundError:
            return None


    def loadFile(self) -> bool:
        try:
            self.__file = open("conn", 'r')
            return True
        except FileNotFoundError:
            return False
    
    def getDBPath(self, key_search):
        if self.__file is not None:
            for line in self.__file:
                if key_search in line:
                    return line.split(key_search)[-1][:-1]
        return None
    
    def __makeBackupBatFile(self) -> bool:
        #need the file to be loaded
        dbPath = self.getDBPath(key_search='M3=')
        pathCommand = "cd %s\n" % self.__getFBBinPath()
        bkpCommand = 'gbak -user SYSDBA -password masterkey "%s" "%s"' % (dbPath, dbPath.replace("DADOS.FDB", "BKP.FBK"))
        
        try:
            batFile = open(self.__bkpFileName, "w")
            batFile.writelines([pathCommand, bkpCommand])
            batFile.close()
            return True
        except:
            return False

    def makeBackup(self) -> bool:
        if self.__makeBackupBatFile():
            try:
                import subprocess
            except ImportError:
                return False
            
            subprocess.call(os.path.join(self.__BASE_DIR, self.__bkpFileName))
            return True
        
        return False