colocados = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
             'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani',
             'Sport', 'Portuguesa', 'Atético Paranaense', 'Vitória')
print(f'Lista de times do Brasileirão: {colocados}')
print(f'Os primeiros 5 colocados são: {colocados[0:5]}')
print(f'Os últimos 4 colocados são: {colocados[:-5:-1]}')
print(f'Os times em ordem alfabética: {sorted(colocados)}')
print(f'O time Guarani aparece na posição {colocados.index("Guarani") + 1}')