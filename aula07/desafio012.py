p = int(input('Qual o \033[1mpreço do produto?\033[m '))
d = p / 100 * 5
pd = p - d
print(f'O preço do produto com \033[1mdesconto\033[m é de \033[4;32m{pd}\033[m reais!')
