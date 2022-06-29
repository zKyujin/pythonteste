v = int(input('Em qual velocidade o seu carro estava? '))
if v >80:
    multa = (v - 80) * 7
    print(f'Você foi multado, e o valor da multa foi de R${multa:.2f}')
else:
    print('Você não foi multado! :D')

