from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos. Portanto, sua categoria será Mirim.')
if 9 < idade <= 14:
    print(f'Você tem {idade} anos. Portanto, sua categoria será Infantil.')
if 14 < idade <= 19:
    print(f'Você tem {idade} anos. Portanto, sua categoria será Junior.')
if idade == 20:
    print(f'Você tem {idade} anos. Portanto, sua categoria será Sênior.')
if idade > 20:
    print(f'VOcê tem {idade} anos. Portanto, sua categoria será Master.')
