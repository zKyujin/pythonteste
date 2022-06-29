#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas.values())
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[0]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end='')
        print() b
    #for k, v in e.items():
       # print(f'O campo {k} tem valor {v}.')
