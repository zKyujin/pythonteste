from desafio115 import funções
arq = 'cursoemvideo.txt'
if not funções.arquivoExiste(arq):
    funções.criarArquivo(arq)
while True:
    print()
    print('-' * 30)
    print('\tMENU PRINCIPAL')
    print('-' * 30)
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2 -\033[m \033[34mCadastrar nova pessoa\033[m')
    print('\033[33m3 -\033[m \033[34mSair do Sistema\033[m')
    try:
        escolha = int(input('\033[1;33mSua opção: \033[m'))
    except:
        print('\033[31mPor favor, digite uma opção válida!\033[m')
    else:
        if escolha == 1:
            funções.lerArquivo(arq)
            continue
        elif escolha == 2:
            funções.cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = funções.leiaint('Idade: ')
            funções.cadastrar(arq, nome, idade)
        elif escolha == 3:
            break
        elif 0 <= escolha > 3:
            print('Por favor, digite uma opção válida.')
            continue