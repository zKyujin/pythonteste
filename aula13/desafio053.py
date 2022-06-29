f = str(input('Digite uma frase: ')).lower().replace(' ', "")
x = f[::-1].strip().lower()
if x == f:
    print(f' Essa frase é sim palíndromo!')
else:
    print(f'\033[31mNÃO\033[m é uma frase palíndromo!')
