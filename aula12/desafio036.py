casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestamensal = casa / (anos * 12)
if prestamensal <= salario * 30 / 100:
    print('Parabéns, o empréstimo foi aprovado!')
    print(f'O valor da prestação mensal vai ser de R${prestamensal:.2f}')
elif prestamensal > salario * 30 / 100:
    print(f'Para pagar uma casa de {casa} em {anos} anos, a prestação será de R${prestamensal:.2f}, o que é mais de 30% '
          f'do seu salário de R${salario}.\n Empréstimo NEGADO!')



