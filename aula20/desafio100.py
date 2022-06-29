from random import randint
numeros = []
def sorteia():
    cont = 0
    print(f'sorteando, 5 valores da lista: ', end='')
    while cont <= 5:
        numeros.append(randint(1, 10))
      #  print(randint(1, 10), end=' ')
        cont += 1
    for valor in numeros:
        print(f'{valor} ', end=' ')
    print('PRONTO!')



def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {numeros}, é de {soma}')



sorteia()
somaPar()

