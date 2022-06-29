somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresmenor20 = 0
for c in range(1, 5):
    print(f'-----{c}ªPESSOA----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maoridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenor20 += 1
mediaidade = somaidade // 4
print(f'A média das idades é de {mediaidade}.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'{mulheresmenor20} mulheres tem menos de 20 anos.')
