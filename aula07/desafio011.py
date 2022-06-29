al = float(input('A parede tem quantos metros de \033[1;33maltura\033[m? '))
l = float(input(' A parede tem quantos metros de \033[1;33mlargura?\033[m '))
a = al * l
t = a / 2
print(f'A área dessa parede é de \033[4;31m{a}m²\033[m e, para pinta-la serão necessários \033[1;34m{t}\033[m litros de tinta.')
