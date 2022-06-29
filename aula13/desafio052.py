n = int(input('Digite um número inteiro: '))
cont = 0
for c in range (1, n + 1):
    print(c, end=' ')
    if n % c == 0:
        print('\033[1:33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
print(f'\033[mO número {n} foi divisível {cont} vezes.')
if cont == 2:
    print('\033[mPortanto, Esse número é primo!')
else:
    print('Portanto, esse número NÃO é primo!')

