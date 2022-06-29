import random
cont = 0
while True:
    print('=-' * 10)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 10)
    n = int(input('Diga um valor: '))
    m = str(input('[Par/Impar]: ')).upper()
    pc = random.randint(1, 10)
    total = n + pc
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if m == resultado:
        print(f'Você jogou {n} e o computador {pc}. Total de {total} DEU {resultado}')
        print('Você venceu, Parabéns!')
    else:
        print(f'Você jogou {n} e o computador {pc}. Total de {total} DEU {resultado}')
        print('Você perdeu!')
        print(f'GAME OVER! Você venceu {cont} vezes')
        break
    cont += 1
