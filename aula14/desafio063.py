print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
cont = 3
n1 = 0
n2 = 1
print(f'{n1}\n{n2}')
while cont <= termos:
    n3 = n1 + n2
    print(f'{n3}')
    n1 = n2
    n2 = n3
    cont +=1
print('Fim')
