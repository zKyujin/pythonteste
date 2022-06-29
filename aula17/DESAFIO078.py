n = []
maior = 0
menor = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {maior} na posição', end='')
for posicao, valor in enumerate(n):
    if n[posicao] == maior:
        print(f'...{posicao}')

print(f'O menor valor digitado foi {menor} na posição', end='')
for posicao, valor in enumerate(n):
    if n[posicao] == menor:
        print(f'...{posicao}')



