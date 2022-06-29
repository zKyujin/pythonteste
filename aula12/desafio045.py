import random
user = str(input('Escolha entre pedra papel e tesoura: ')).lower()
opções = 'pedra', 'papel', 'tesoura'
machine = random.choice(opções)
print(f'A máquina escolheu {machine}')
if user == 'pedra' and machine == 'pedra' or user == 'papel' and machine == 'papel' or user == 'tesoura' and machine == 'tesoura':
    print(f'Ambos escolheram {user}, portanto, o resultado foi \033[1:33mempate\033[m!')
if user == 'pedra' and machine == 'tesoura' or user == 'tesoura' and machine == 'papel' or user == 'papel' and machine == 'pedra':
    print(f'Você \033[1:34mvenceu\033[m, Parabéns!')
if machine == 'pedra' and user == 'tesoura' or machine == 'tesoura' and user == 'papel' or machine == 'papel' and user == 'pedra':
    print('Você \033[1:31mperdeu\033[m! ç.ç')

