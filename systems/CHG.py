from database.FirebirdInterface import Interface
from file.File import File

class CHG(Interface):
    
    def __init__(self) -> None:
        self.__db_path = self.__loadDBPath()

        self.__get_produtos ="select produto.pro_codigo, produto.pro_precomg from produto"

    def __loadDBPath(self) -> None:
        f = File()
        f.loadFile()
        return f.getDBPath(key_search='CHG=')
    
    def start(self) -> bool:
        super().__init__(database=self.__db_path, databaseAlias='CHG Database')
        status = super().createConnection()
        # if status is False: exit
        return status
    
    def end(self) -> None:
        super().closeConnection()
    
    def getProdutos(self):
        makeDict = lambda row: {'codigo': str(int(row[0])),'preco': float(row[1])}
        result = self.select(query=self.__get_produtos)
        produtos = []
        if result is not None:
            for row in result:
                produtos.append(makeDict(row))
        
        return produtos