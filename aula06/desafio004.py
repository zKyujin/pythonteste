n = input('Digite algo: ')

print('O tipo primitivo desse valor é: \033[31m{}'.format(type(n)))
print('Só tem espaços? \033[32m{}'.format(n.isspace()))
print('É um número? \033[33m{}'.format(n.isnumeric()))
print('É alfabético? \033[34m{}'.format(n.isalpha()))
print('É alfanumérico? \033[35m{}'.format(n.isalnum()))
print(f'Está em maiúsculas? \033[36m{n.isupper()}')
print('Está em minúsculas? ''\033[37m', n.islower())
print('Está capitalizada? ''\033[1;37', n.istitle())






