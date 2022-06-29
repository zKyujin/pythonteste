import csv
novapessoa = {}
pessoascadastradas = []
teste = []
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
            print(novapessoa)
            print(pessoascadastradas)
            with open('pessoascadastradas.csv', newline='') as f:
                reader = csv.reader(f)
                for row in pessoascadastradas:
                    print(f'{row}', end='\t')

            continue
        if escolha == 2:
            try:
                novapessoa['Nome'] = str(input('Nome: ')).strip()
            except Exception as erro:
                print(f'Tivemos um erro de {erro.__class__}, por favor, tente novamente.')
                try:
                    novapessoa['Nome'].isalpha()
                except:
                    print('\033[31mERRO! Digite um nome válido!\033[m')
            while True:
                try:
                    novapessoa['Idade'] = int(input('Idade: '))
                except (TypeError, ValueError):
                    print('\033[31mERRO! Digite um número inteiro válido!\033[m')
                finally:
                    with open('pessoascadastradas.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(novapessoa)
                    pessoascadastradas.append(novapessoa["Nome"])
                    pessoascadastradas.append(novapessoa["Idade"])
                    print(f'Novo registro de {novapessoa["Nome"]} adicionado.')
                    break
        if escolha == 3:
            break
        if 0 <= escolha > 3:
            print('Por favor, digite uma opção válida.')
            continue