from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$')
print(moeda.resumo(p, 10))
