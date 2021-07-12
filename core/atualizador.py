from datetime import datetime
from systems.CHG import CHG
from systems.M3 import M3
from time import sleep

class Atualizador():

    def __init__(self) -> None:
        self.__M3Interface = M3()
        self.__CHGInterface = CHG()

        self.__relatorio = list()
        self.__produtosCHG = None

    def startM3(self):
        status = self.__M3Interface.start()
        return status

    def startCHG(self):
        status = self.__CHGInterface.start()
        return status

    def __endM3(self):
        self.__M3Interface.end()
    
    def __endCHG(self):
        self.__CHGInterface.end()

    def startDB(self):
        print('Tentando se conectar com as bases de dados ...')
        sleep(3)
        self.startM3()
        sleep(1)
        self.startCHG()
        sleep(1)

    def endDB(self):
        print('Encerrando conexão com as bases de dados')
        sleep(2)
        self.__endM3()
        sleep(.5)
        self.__endCHG()
        sleep(.5)

    def __loadProdutosCHG(self):
        self.__produtosCHG = self.__CHGInterface.getProdutos()
    
    def __getDataForUltimaAlteracao(self):
        return datetime.now().strftime('%d.%m.%Y %H:%M')

    def __atualizado(self, cod_m3, custo_antigo, custo_novo):
        return '[%s ATUALIZADO] => CUSTO ANTIGO: %07.2f - CUSTO NOVO: %07.2f' % (cod_m3, custo_antigo, custo_novo)

    def __naoAtualizado(self, cod_m3, custo_m3, custo_chg):
        return '[%s NAO ATUALIZADO] => CUSTO DA M3: %07.2f SUPERIOR OU IGUAL AO CUSTO CHG: %07.2f' % (cod_m3, custo_m3, custo_chg)

    def __erroAoAtualizar(self, cod_m3):
        self.__relatorio.append('[%s NAO ATUALIZADO] - FALHA AO ATUALIZAR\n' % cod_m3)
        return '[%s NAO ATUALIZADO] - FALHA AO ATUALIZAR' % cod_m3

    def getRelatorio(self):
        return self.__relatorio

    def detalhar(self, a, e, n):
        print('%d PRODUTOS ATUALIZADOS' % a)
        print('%d PRODUTOS NAO ENCONTRADOS' % n)
        print('%d PRODUTOS COM ERRO AO ATUALIZAR' % e)

    def atualizar(self, tkList):
        self.__loadProdutosCHG()

        total = 0
        atualizados = 0
        naoEncontrados = 0
        erroAoAtualizar = 0

        for produto in self.__produtosCHG:
            custo_chg = produto['preco']
            codigo_chg = produto['codigo']

            produto_m3 = self.__M3Interface.getProduto(cod_fabricante=codigo_chg)

            if produto_m3 is not None:

                if custo_chg > produto_m3['custo']:
                    novo_valor_venda = custo_chg * 2.2
                    status = self.__M3Interface.updateProduto(
                        custo=custo_chg,
                        venda=novo_valor_venda,
                        ult_alteracao=self.__getDataForUltimaAlteracao(),
                        cod_produto=produto_m3['produto']
                    )
                    if status:
                        text = self.__atualizado(produto_m3['produto'], produto_m3['custo'], custo_chg)
                        # tkList.insert("end", text)
                        # tkList.itemconfig(total, foreground='green')
                        atualizados += 1
                    else:
                        text = self.__erroAoAtualizar(produto_m3['produto'])
                        # tkList.insert("end", text)
                        # tkList.itemconfig(total, foreground='red')
                        erroAoAtualizar += 1
                else:
                    text = self.__naoAtualizado(produto_m3['produto'], produto_m3['custo'], custo_chg)
                    # tkList.insert("end", text)
                    # tkList.itemconfig(total, foreground='deep sky blue')
            else:
                self.__relatorio.append('[CODIGO CHG %s NAO ENCONTRADO NA BASE DE DADOS M3]\n' % codigo_chg)
                text = '[CODIGO CHG %s NAO ENCONTRADO NA BASE DE DADOS M3]' % codigo_chg
                # tkList.insert("end", text)
                # tkList.itemconfig(total, foreground='yellow')
                naoEncontrados += 1
            print(text)
            total += 1

        self.detalhar(atualizados, erroAoAtualizar, naoEncontrados)
        
