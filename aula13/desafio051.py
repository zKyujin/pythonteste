soma = 0
n = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão dessa P.A: '))
for c in range(1, 10):
    if soma == 0:
        soma = n + r
        print(f'{n}')
    print(f'{soma}')
    soma = soma + r
