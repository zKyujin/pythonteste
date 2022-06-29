lista = [[], [], []]
cont = soma = coluna3 = maior = 0
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
for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
            soma += lista[l][c]
        if c == 2:
            coluna3 += lista[l][c]
        if l == 1:
            if lista[1][c] > maior:
                maior = lista[1][c]
print(f'{lista[0]}\n'
      f'{lista[1]}\n'
      f'{lista[2]}\n')
print(f'A soma de todos os valores pares foi de: {soma}')
print(f'A soma dos valores da terceira coluna é de: {coluna3}')
print(f'O maior dos valores da segunda linha é:{maior} ')
