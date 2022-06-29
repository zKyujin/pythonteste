peso = int(input('Peso em KG: '))
altura = float(input('Altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu imc é de {imc:.2f}. Você está \033[1:33mabaixo\033[m do peso.')
if 18.5 <= imc < 25:
    print(f'Seu imc é de {imc:.2f}. Você está no \033[1:34mpeso ideal\033[m, parabéns!')
if imc >= 25 and imc < 30:
    print(f'Seu imc é de {imc:.2f}. Cuidado, você está com \033[1:33msobrepeso\033[m')
if imc >= 30 and imc <= 40:
    print(f'Seu imc é de {imc:.2f}. Cuidado, você está no estado de \033[1:31mobesidade\033[m')
if imc > 40:
    print(f'Seu imc é de {imc:.2f}. Cuidado, você está no estado de \033[1:31mobesidade mórbida\033[m!')


