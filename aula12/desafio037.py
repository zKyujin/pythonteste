import math
n = int(input('Digite um número inteiro qualquer: '))
conversao = int(input('Escolha qual será a base da conversão, sendo:\n1 para binário \n2 para octal\n3 para '
                      'hexadecimal\n:'))
if conversao == 1:
    print(f'O numero {n} em binário é representado como:{bin(n)}')
elif conversao == 2:
    print(f'O número {n} em octal é representado como:{oct(n)}')
elif conversao ==3:
    print(f'O número {n} em hexadecimal é representado como: {hex(n)}')

