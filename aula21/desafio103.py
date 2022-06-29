def ficha(nome=0, gols=0):
    """
    :param nome: nome do jogador.
    :param gols: quantidade de gols feitos por ele.
    :return:
    """
    nome = str(input('Nome do jogador: '))
    gols = str(input('Número de gols: '))
    if nome == '':
        nome = '<desconhecido>'
    if gols.isalpha():
        gols = int(0)
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha()

#Solução Guanabara
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)




