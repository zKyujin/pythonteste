r1 = int(input('Qual o comprimento da primeira reta em cm? '))
r2 = int(input('Qual o comprimento da segunda reta em cm? '))
r3 = int(input('Qual o comprimento da terceira reta em cm? '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível sim formar um triângulo com essas retas!')
else:
    print('NÃO é possível formar um triângulo com essas retas :c')
