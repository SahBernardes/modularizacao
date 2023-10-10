''' ex 109:
Modifique as funções que form criadas no desafio 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
'''


def aumentar(v=0, taxa=0, format=False):
    """
    -> aumentar 'tantos'% do preço:
    :param v: valor do produto
    :param taxa: taxa do produto
    :param format: formatação do preço em real
    :return: o resultado do valor e a sua formatação em real
    """
    r = v + (v * taxa / 100)
    return r if format is False else moeda(r)


def diminuir(v=0, taxa=0, formato=False):
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


def metade(v, formato=False):
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


