'''112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função
leiaInt(), mas com uma validação de dados para aceitar apenas
valores que seja monetários.
'''


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! \"{entrada}\" é um preço invalido!')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('\033[0;31mErro! digite um n° inteiro valido: \033[m')
        if ok:
            break
    return v
