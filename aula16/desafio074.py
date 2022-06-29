import random
n = random.randrange(1, 1000)
n1 = random.randrange(1, 1000)
n2 = random.randrange(1, 1000)
n3 = random.randrange(1, 1000)
n4 = random.randrange(1, 1000)
tupla = n, n1, n2, n3, n4
print(f'Os valor sorteados foram: {tupla}')
maior = menor = n
if maior < n1:
    maior = n1
if maior < n2:
    maior = n2
if maior < n3:
    maior = n3
if maior < n4:
    maior = n4
if menor > n1:
    menor = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
if menor > n4:
    menor = n4

print(f'O maior valor é {maior} e o menor é {menor}')