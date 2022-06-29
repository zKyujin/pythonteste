def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(4, 5)
soma(b=8, a=9)
soma(2, 1)


def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM')


# Programa Principal
contador(2, 1, 8)
contador(8, 0)
contador(4, 4, 7, 8)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
valores = [6, 3, 9, 5, 2, 0]
dobra(valores)
print(valores)

def somar(* valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores}, temos {s}')


# Programa Principal
somar(1, 3)
somar(1, 4, 5)











