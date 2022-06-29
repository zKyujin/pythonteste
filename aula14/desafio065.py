cont = soma = n = maior = menor = media = 0
resposta = ''
while resposta in ('s').upper():
    n1 = int(input('Digite um número: '))
    if n < n1:
        maior = n1
        menor = n
    if n > n1:
        maior = n
        menor = n1
    soma += n1
    cont += 1
    media = soma / cont
    n = n1
    resposta = str(input('Quer continuar? [S/N]')).upper()
print(f'Você digitou {cont} números e a média foi {media}'
      f'O maior valor foi {maior} e o menor foi {menor}')

