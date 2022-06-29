import csv
from desafio115 import funções
while True:
    resposta = funções.menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')