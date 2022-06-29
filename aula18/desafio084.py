pessoas = list()
pessoa = list()
pesados = list()
leves = list()
maiorpeso = menorpeso = quantpessoas = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso [KG]: ')))
    continuar = input('Quer continuar? [S/N]').lower()
    quantpessoas += 1
    if len(pessoas) == 0:
        maiorpeso = menorpeso = pessoa[1]
    else:
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    if continuar not in 'sn':
        continuar = input('Quer continuar? [S/N]').lower()
    if continuar in 'Nn':
        break
print(pessoas)
print(f'Foram cadastradas {quantpessoas} pessoas.\n'
      f'O maior peso foi de {maiorpeso}KG, que é o peso de:', end= '')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'O menor peso foi de {menorpeso}, que é o peso de: ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
