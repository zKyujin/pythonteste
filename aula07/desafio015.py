d = int(input('Quantos \033[32mdias\033[m alugados? '))
km = int(input('Quantos \033[32mKm\033[m rodados? '))
p = 60 * d + 0.15 * km

print(f'O preço a pagar é de \033[1;31mR${p:.2f}')
