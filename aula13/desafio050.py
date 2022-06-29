cont = 0
soma = 0
for c in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(f'Entre os números digitados, {cont} eram par, e a soma de todos eles é igual a {soma}')
