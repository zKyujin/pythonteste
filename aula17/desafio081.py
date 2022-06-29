n = []
while True:
    n.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar? [S/N] ')).lower()
    if c not in 'sn':
        c = str(input('Quer continuar? [S/N] ')).lower()
    if c == 'n':
        print(f'Foram digitados {len(n)} valores')
        n.sort(reverse=True)
        print(f'A lista de valores em ordem decrescente é: {n}')
        if 5 in n:
            print(f'O valor 5 \033[1mestá\033[m na lista, na posição {n.index(5)}.')
        else:
            print('O valor 5 \033[1mnão está\033[m na lista.')
        break
