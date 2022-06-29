jogador = {}
partidas = list()
time = list()
total = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['totalgols'] = sum(partidas)
    time.append(jogador.copy())
    print(jogador)
    print(time)
    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print('cod', end='')
for l in jogador.keys():
    print(f'{l}:<15', end='')
print()
print('-' * 40)
for c, i in enumerate(time):
        print(f'{c:>3}', end='')
        for d in i.values():
            print(f'{str(d):<15}', end='')
        print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo{i+1} fez {g} gols.')
        print('-' * 40)
print('>> VOLTE SEMPRE <<')
