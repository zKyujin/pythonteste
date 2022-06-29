from datetime import date
ano = int(input('Em qual ano você nasceu? '))
idade = date.today().year - ano
print(input(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.'))
if idade == 18:
    print('Esse é o seu ano de alistamento. Você deve se alistar imediatamente!')
if idade > 18:
    print(f'Você já tem {idade} anos! Já passou do tempo de você se alistar!')
if idade < 18:
    anosquefaltam = 18 - idade
    anodealistamento = ano + 18
    print(f'Você atualmente está com {idade} anos! Para você se alistar ainda faltam {anosquefaltam} anos, ou seja, será no ano de {anodealistamento}!')

