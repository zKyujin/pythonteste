n = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
menu = 0
resposta = 0
while menu != 5:
    menu = int(input('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos valores\n[5] - Sair do programa\n\n: '))
    if menu == 1:
        resposta = n + n2
        print(f'O resultado da soma é de {resposta}')
    if menu == 2:
        resposta = n * n2
        print(f'O resultado da multiplicação é de {resposta}')
    if menu == 3:
        if n > n2:
            maior = n
            print(f'O maior é {maior}')
        else:
            maior = n2
            print(f'O maior é {maior}')
    if menu == 4:
        n = int(input('Digite um valor: '))
        n2 = int(input('Digite mais um valor: '))
    if menu == 5:
        print('FIM')
