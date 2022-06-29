s = float(input('Qual o seu salário? '))
if s > 1250.00:
    aumento = s + s * 10 / 100
    print(f'O seu novo salário com aumento de 10%, será de: R${aumento}')
if s <= 1250.00:
    aumento = s + s * 15 / 100
    print(f'O seu novo salário com aumento de 15%, será de: R${aumento}')

