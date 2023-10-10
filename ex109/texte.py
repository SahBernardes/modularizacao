import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Com almento de {t}%, temos {moeda.aumentar(p, True, True)}')
print(f'com a diminuição de {t}%, temos {moeda.diminuir(p, True, True)}')
