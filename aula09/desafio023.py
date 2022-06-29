numero = str(input('Digite um número de 0 a 9999: '))
unidade = numero[3:]
dezena = numero[2:3]
centena = numero[1:2]
milhar = numero[0:1]
print(f'Unidade:{unidade}  \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')