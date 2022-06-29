maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso em KG: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso foi de {maior}Kg, e o menor de {menor}Kg')
