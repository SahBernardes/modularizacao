import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Com almento de {t}%, R${moeda.aumentar(p, t):.2f}')
print(f'com a diminuição de {t}%, R${moeda.diminuir(p, t):.2f}')
