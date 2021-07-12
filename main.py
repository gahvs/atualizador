
from core.atualizador import Atualizador

obj = Atualizador()
obj.startDB()
obj.atualizar([])

relatorio = obj.getRelatorio()

with open('nao-atualizados.txt', 'w') as f:
    f.write('%d PRODUTOS NAO ATUALIZADOS\n\n' % len(relatorio))
    for line in relatorio:
        f.write(line)

obj.endDB()