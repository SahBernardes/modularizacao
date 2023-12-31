'''ex: 108
Exercício Python 108: Adapte o código do desafio #107, criando 
uma função adicional chamada moeda() que consiga mostrar os 
números como um valor monetário formatado.
'''


def aumentar(v=0, taxa=0):
    r = v + (v * taxa / 100)
    return r


def diminuir(v=0, taxa=0):
    r = v - (v * taxa / 100)
    return r


def dobro(v=0):
    r = v * 2
    return r


def metade(v):
    r = v/2
    return r


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


