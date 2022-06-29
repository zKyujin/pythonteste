n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
a = n1 + n2
m = n1 * n2
d = n1 / n2
s = n1 - n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print(f'A soma é {a}, \n o produto é {m} \n e a divisão é {d:.3f}', end=' ')
print(f'A subtração é {s}, a potenciação é {p}, a divisão inteira é {di} e o resto é {r}')

