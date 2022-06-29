import datetime
dicio = dict()
dicio['nome'] = str(input('Nome: '))
dicio['ano de nascimento'] = int(input('Ano de nascimento: '))
dicio['carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
dicio['idade'] = datetime.datetime.now().year - dicio['ano de nascimento']
if dicio['carteira de trabalho'] != 0:
    dicio['ano de contratação'] = int(input('Ano de contratação: '))
    dicio['salário'] = int(input('Salário: R$'))
    dicio['aposentadoria'] = dicio['ano de contratação'] + 35 - dicio['ano de nascimento']
del dicio['ano de nascimento']
print(dicio)
for c, i in dicio.items():
    print(f'{c} tem o valor {i}')