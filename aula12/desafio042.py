r1 = int(input('Qual o comprimento da primeira reta em cm? '))
r2 = int(input('Qual o comprimento da segunda reta em cm? '))
r3 = int(input('Qual o comprimento da terceira reta em cm? '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível sim formar um triângulo com essas retas!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Esse triângulo é equilátero, pois tem todos os lados iguais!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Esse triângulo é isósceles, pois tem dois lados iguais!')
    else:
        print('Esse triângulo é escaleno, pois todos os lados são diferentes!')
else:
    print('NÃO é possível formar um triângulo com essas retas :c')
