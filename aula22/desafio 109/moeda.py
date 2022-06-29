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
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço Analisado: {p:>5}')
    print(f'Dobro do preço: {dobro(p)}')
    print(f'Metade do preço: {metade(p)}')
    print(f'{a}% de aumento: {aumentar(p), (a)}')
    print(f'{r}% de redução: {diminuir(p), (a)}')