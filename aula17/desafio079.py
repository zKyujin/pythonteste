n = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in n:
        print('Valor duplicado! Não vou adicionar...')
    if valor not in n:
        n.append(valor)
    c = str(input('Quer continuar? [S/N]')).lower()
    if c == 'n':
        n.sort()
        print(f'Você digitou os valores {n}')
        break



