import random
prim = input('Digite o nome do primeiro aluno: ')
seg = input('Digite o nome do segundo aluno: ')
terc = input('Digite o nome do terceiro aluno: ')
quart = input('Digite o nome do quarto aluno: ')
sorteado = random.choice([prim, seg, terc, quart])
print(f'O aluno sorteado foi {sorteado}! Parabéns!')



