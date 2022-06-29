c = ['\033[0;30m', #padrao
     '\033[1;31m', #vermelho
     '\033[1;33m']


def help2(biblioteca):
    help(biblioteca)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# Programa Principal
a = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    a = str(input('Função ou Biblioteca > '))
    if a.upper() == 'FIM':
        break
    else:
        help2(a)
titulo('ATÉ LOGO!', cor=1)
