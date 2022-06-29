import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
ordem = [a, b, c, d]
random.shuffle(ordem)
#ordem = random.sample([a, b, c, d], counts=[1, 1, 1, 1],k=4)
print(f'A ordem de apresentação vai ser: {ordem}')

