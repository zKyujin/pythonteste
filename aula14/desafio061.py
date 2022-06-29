n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n2 = 0
termos = 0
while termos != 9:
    if n2 == 0:
        print(f'{n}')
        n2 = n + r
        print(f'{n2}')
        termos += 1
    else:
        n2 += r
        print(f'{n2}')
        termos += 1