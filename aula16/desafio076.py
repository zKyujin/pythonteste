listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 50)
print(' ' * 15, '\033[1mLISTAGEM DE PREÇOS\033[m')
print('-' * 50)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', "R$", end='')
    else:
        print(f'{listagem[c]:>6.2f}')