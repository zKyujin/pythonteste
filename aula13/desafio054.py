import datetime
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Ano:'))
    idade = datetime.date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Dessas 7 pessoas, {maior} já atingiram a maioridade e {menor} ainda não.')



