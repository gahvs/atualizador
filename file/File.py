class File:

    def __init__(self) -> None:
        self.__file = None

    def loadFile(self) -> bool:
        try:
            self.__file = open("conexao.txt", 'r')
            return True
        except FileNotFoundError:
            return False
    
    def getDBPath(self, key_search):
        if self.__file is not None:
            for line in self.__file:
                if key_search in line:
                    return line.split(key_search)[-1][:-1]
        return None