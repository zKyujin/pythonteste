import random
n = int(random.choice([0, 1, 2, 3, 4, 5]))
n2 = int(input('Digite um número de 0 a 5: '))
print(f'O número escolhido pela máquina foi {n}!')
print('Parabéns, você venceu!' if n == n2 else 'Você perdeu ç.ç.')
