import random
n = int(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
n2 = ''
palpites = 0
while n2 != n:
    n2 = int(input('Digite um número entre 0 e 10: '))
    palpites += 1
print(f'Você venceu, parabéns! Foram necessários {palpites} palpites para você acertar.')
