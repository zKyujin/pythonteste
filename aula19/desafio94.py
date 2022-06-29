pessoa = dict()
todaspessoas = list()
idade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    todaspessoas.append(pessoa.copy())
    idade += pessoa['idade']
    while True:
        continuar = str(input('Você quer continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(todaspessoas)} pessoas')
print(f'A média de idade do grupo é de {idade / len(todaspessoas):.1f} anos.')
print(f'As mulheres cadastradas foram:')
for c, v in enumerate(todaspessoas):
    if todaspessoas[c]['sexo'] == 'F':
        print(f'{todaspessoas[c]["nome"]}', end=', ')
print()
print(f'As pessoas com idade acima da média foram:')
for c, v in enumerate(todaspessoas):
    if todaspessoas[c]['idade'] > idade / len(todaspessoas):
        print(f'{todaspessoas[c]}')
    