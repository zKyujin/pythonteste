galera = [['João', 19], ['Ana', 22], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
maior = menor = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'{maior} são maiores de idade e {menor} são menores de idade')
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
