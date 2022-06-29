d = int(input('Qual a distância da viagem em Km? '))
if d <= 200:
    p = d * 0.50
    print(f'O preço da passagem é de R${p:.2f}')
else:
    p = d * 0.45
    print(f'O preço da passagem é de R${p:.2f}')
