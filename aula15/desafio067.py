multiplicador = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Programa tabuada encerrado. Volte sempre!')
        break
    while multiplicador < 11:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1
    if multiplicador >= 11:
        multiplicador = 1

