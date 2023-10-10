''' ex  111: Crie um pacote chamado utilidadesCeV que tenha dois
módulos internos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108 e 109 para o primeiro
pacote e mantenha tudo funcionando.
'''


def aumentar(v=0, taxa=10, formato=False):
    """
    -> aumentar 'tantos'% do preço:
    :param v: valor do produto
    :param taxa: taxa do produto
    :param format: formatação do preço em real
    :return: o resultado do valor e a sua formatação em real
    """
    r = v + (v * taxa / 100)
    return r if formato is False else moeda(r)


def diminuir(v=0, taxa=5, formato=False):
    """
    -> diminuir 'tantos'% do preço:
    :param v: valor do produto
    :param taxa: taxa de diminuição
    :param formato: formato do preço em real
    :return: o resultado do valor e a sua formatação em real
    """
    r = v - (v * taxa / 100)
    return  r if formato is False else moeda(r)


def dobro(v=0, formato=False):
    """
    -> dobrar o Preço:
    :param v: valor do produto
    :param formato: formato do preço em real
    :return: o resultado do valor e sua formatação em real
    """
    r = v * 2
    return r if not formato else moeda(r)


def metade(v=0, formato=False):
    '''
    -> diminuição da metade do preço:
    :param v: valor  do produto
    :param formato:  formato do preço em real
    :return:  resultado do valor e sua formatação em real
    '''
    r = v/2
    return r if not formato else moeda(r)


def moeda(v=0, moeda='R$'):
    """
    -> formatação do valor:
    :param v: valor do produto
    :param moeda: formatação da moeda em si para real
    :return: retorno do resultado
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(v=0, taxa=0):
    """
    -> retorna o resumo final de tds as analises anteriores
    :param v: valor do produto
    :param taxa: taxa do produto
    :return: retornar as analizes
    :print: trazendo a 'materialização' desses valores e explicitando na tela
    """
    print('*' * 30)
    print('RESUMO DO VALOR!'.center(30))
    print('*' * 30)
    print(f'preço analizado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'Aumentando {taxa}%: \t{aumentar(v, True, True)}')
    print(f'Reduzindo {taxa}%: \t\t{diminuir(v, True, True)}')
    print('*' * 30)
