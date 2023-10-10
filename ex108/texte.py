import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com almento de {t}%, {moeda.moeda(moeda.aumentar(p)), t}')
print(f'com a diminuição de {t}%, {moeda.moeda(moeda.diminuir(p)), t}')
