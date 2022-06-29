def aumentar(n, p):
    aumento = n * p / 100
    n += aumento
    return n


def diminuir(n, p):
    porcentagem = n * p / 100
    n -= porcentagem
    return n


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
