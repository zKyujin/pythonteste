dicio = {}
gols = list()
total = 0
dicio['nome'] = str(input('Nome do jogador: '))
dicio['jogos'] = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for c in range(0, dicio['jogos']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += gols[c]
dicio['gols'] = gols
print(dicio)
for c, i in dicio.items():
    print(f'O campo {c} tem valor {i}')

print(f'O jogador {dicio["nome"]} jogou {dicio["jogos"]} partidas.')
for c in range(0, dicio['jogos']):
    print(f'Na partida {c}, fez {dicio["gols"][c]} gols.')
