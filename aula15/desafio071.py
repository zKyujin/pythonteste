print('=' * 20)
print(' ' * 4, 'BANCO CEV')
print('=' * 20)
resultado50 = resultado20 = resultado10 = resultado1 = resto = 0
while True:
    valor = int(input('Valor a ser sacado: R$'))
    if valor % 50 == 0:
        resultado50 = valor % 50
    if valor % 50 != 0:
        resultado50 = valor // 50
        resto = valor % 50
    if resultado50 != 0:
        resultado20 = resto // 20
        resto = resto % 20
    if resultado20 != 0:
        resultado10 = resto // 10
        resto = resto % 10
    if resto != 0:
        resultado1 = resto // 1
    print(f'Total de {resultado50} cédulas de R$50\n'
          f'Total de {resultado20} cédulas de R$20\n'
          f'Total de {resultado10} cédulas de R$10\n'
          f'Total de {resultado1} cédulas de R$1')
    break

