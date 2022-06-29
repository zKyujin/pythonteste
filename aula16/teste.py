
n1 = tuple(int(input('Digite um número: ')) for n in range(4))
print(n1)
print(f'O valor 9 aparece {n1.count(9)} vezes')
if 3 in n1: print(f'O valor 3 apareceu pela primeira vez na posição {n1.index(3)+1}')
print('Os valores pares digitados são:',end=' ')
for n in n1:
    if n % 2 == 0: print(n, end=' ')