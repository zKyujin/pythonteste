valor = float(input('Qual o preço do produto? R$'))
forma = int(input(
    "Digite a forma de pagamento, sendo:\n1 para dinheiro ou cheque (10% de desconto)\n2 para à "
    "vista no cartão (5% de desconto)\n3 para em até 2x no cartão (preço normal)\n4 para 3x ou "
    "mais no cartão (20% de juros)\n"))
if forma == 1:
    print(f'O preço do produto com 10% de desconto é de: R${valor - valor * 10 / 100:.2f}')
if forma == 2:
    print(f'O preço do produto com 5% de desconto é de: R${valor - valor * 5 / 100:.2f}')
if forma == 3:
    print(f'O preço do produto será normal com essa forma de pagamento, sendo no caso, de R${valor:.2f}')
if forma == 4:
    print(f'O preço do cada produto com os 20% de juros, vai ser de R${valor + valor * 20 / 100:.2f}')

