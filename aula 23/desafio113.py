def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

# Programa Principal
n = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n}')
print(f'Você acabou de digitar o número real {m}')
