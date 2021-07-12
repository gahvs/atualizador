from database.FirebirdInterface import Interface
from file.File import File

class M3(Interface):
    def __init__(self) -> None:
        self.__db_path = self.__loadDBPath()

        self.__get_produto = ''' 
            select produtos.produto, produtos.empresa, produtos.custo, produtos.lucro, produtos.venda, produtos.cod_fabricante from produtos
            where
            produtos.cod_fabricante LIKE '%%%s'
        '''
        self.__update_produto = '''
            update produtos set produtos.custo = %.2f, produtos.lucro = %.2f, produtos.venda = %.2f, produtos.ultima_alteracao = '%s'
            where produtos.produto = %s
        '''

    def __loadDBPath(self) -> None:
        f = File()
        f.loadFile()
        return f.getDBPath(key_search='M3=')

    def start(self) -> None:
        super().__init__(database=self.__db_path, databaseAlias='M3 Database')
        status = super().createConnection()
        if status is False: exit
    
    def end(self) -> None:
        super().closeConnection()

    def getProduto(self, cod_fabricante):
        query = self.__get_produto % cod_fabricante
        resultQuery = self.select(query=query)
        if len(resultQuery):
            result = resultQuery[0]
            return {
                'produto': result[0],
                'empresa': result[1],
                'custo': float(result[2]) if result[2] is not None else 0.0,
                'lucro': float(result[3]) if result[3] is not None else 0.0,
                'venda': float(result[4]) if result[4] is not None else 0.0,
                'cod_fabricante': result[5]
            }
        else:
            return None
    
    def updateProduto(self, custo, venda, ult_alteracao, cod_produto):
        query = self.__update_produto % (custo, venda, 120.00, ult_alteracao, cod_produto)
        status = self.execute(query=query)
        return status
