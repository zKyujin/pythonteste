print('-' * 25)
print('LOJA SUPER BARATÃO')
print('-' * 25)
soma = maiorquemil = preço = barato = cont  = 0
nome = ''
continuar = 'a'

while True:
    produto = str(input('Nome do produto: ')).lower()
    preço = int(input('Preço: R$'))
    soma += preço
    if preço > 1000:
        maiorquemil += 1
    if cont == 1:
        barato = preço
        nome = produto
    if barato > preço:
        barato = preço
        nome = produto
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).lower()
    if continuar == 'n':
        print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
        print(f'O total da compra foi de R${soma:.2f}\n'
              f'Temos {maiorquemil} produtos custando mais de R$1000.00\n'
              f'O produto mais barato foi {nome} que custa R${barato:.2f}')
        break
    continuar = 'a'
    cont += 1

