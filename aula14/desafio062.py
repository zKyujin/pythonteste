n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termos = n
cont = 1
mais = 10
total = 0
while mais !=0:
    total += mais
    while cont <= total:
        print(f'{termos}', end=' - ')
        termos += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Fim')

