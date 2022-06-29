def aumentar(n=0, p=0, formato=False):
    res = n + (n * p / 100)
    return res if formato is False else moeda(res)


def diminuir(n=0, p=0, formato=False):
    res = n - (n * p / 100)
    return res if formato is False else moeda(res)

def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)

def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(p, a, r):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de redução: \t{diminuir(p, a, True)}')