''' ex: 107
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.
'''


def aumentar(v, taxa):
    r = v + (v * taxa / 100)
    return r


def diminuir(v, taxa):
    r = v - (v * taxa / 100)
    return r


def dobro(v):
    r = v * 2
    return r


def metade(v):
    r = v / 2
    return r
