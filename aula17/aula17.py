#comandos para lista
num = [2, 3, 4, 5, 6]
num[3] = 9
num.append(7)
num.sort(reverse=True)
num.insert(4, 10)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(8)
valores.append(7)
for v in valores:
    print(f'{v}...')

#Método para criar uma lista com o que o usuário digita
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#Método para mostrar qual valor está em cada posição
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}...')
print('Cheguei ao fim da lista')