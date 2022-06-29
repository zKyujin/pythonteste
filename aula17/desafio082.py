impar = []
par = []
a = []
while True:
    a.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).lower()
    if resposta not in 'sn':
        resposta = str(input('Quer continuar? [S/N] ')).lower()
    if resposta == 'n':
        for posicao, valor in enumerate(a):
            if a[posicao] % 2 == 0:
                par.append(valor)
            if a[posicao] % 2 != 0:
                impar.append(valor)
        print(f'Os valores digitados foram: {a}\n'
              f'Destes valores, são pares: {par}\n'
              f'E são ímpares: {impar}')
        break

