dicio = dict()
dicio['nome'] = str(input('Nome: '))
dicio['média'] = float(input('Média: '))
if dicio['média'] >= 7:
    dicio['situação'] = ('Aprovado')
else:
    dicio['situação'] = ('Reprovado')
for c, i in dicio.items():
    print(f'{c.title()} é igual a {i}')
