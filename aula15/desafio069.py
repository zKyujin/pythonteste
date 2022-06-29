cont = homens = mulheresmenosde20 = 0
sexo = 'a'
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F]')).lower()
    print('-' * 20)
    r = str(input('Quer continuar? [S/N] ')).lower()
    print('-' * 20)
    if sexo == 'f' and idade < 20:
        mulheresmenosde20 += 1
    if idade > 18:
        cont += 1
    if sexo == 'm':
        homens += 1
    sexo = 'a'
    if r == 'n':
        print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
        print(f'Total de pessoas com mais de 18 anos: {cont}\n'
              f'Ao todo temos {homens} homens cadastrados\n'
              f'E temos {mulheresmenosde20} mulheres com menos de 20 anos')
        break



