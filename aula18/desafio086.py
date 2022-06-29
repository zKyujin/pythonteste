lista = [[], [], []]
cont = 0
for c in range(0, 9):
    if c <= 2:
        lista[0].append(int(input(f'Digite um valor para [{c-c}, {cont}]: ')))
    if 5 >= c > 2:
        lista[1].append(int(input(f'Digite um valor para [{c-c+1}, {cont}]: ')))
    if 8 >= c > 5:
        lista[2].append(int(input(f'Digite um valor para [{c-c+2}, {cont}]: ')))
    if c >= 9:
        break
    cont += 1
    if cont > 2:
        cont = 0
print(f'{lista[0]}\n'
      f'{lista[1]}\n'
      f'{lista[2]}')

#SOLUÇÃO GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()