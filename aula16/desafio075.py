n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))
num = (n1, n2, n3, n4)
print(f'Você digitou os valores {num}')
# cont = 0
# for c in num:
# if c == 9:
# cont +=1
print(f'O valor nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 está na posição {num.index(3)}')
else:
    print(f'Não foi digitado um valor que contenha o número 3')
for n in num:
    if n % 2 == 0:
        print(f'Os valores pares são: {n}', end=' ')
    else:
        print('Nenhum valor par foi digitado')
        break
