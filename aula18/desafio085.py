todosvalores = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite um valor[{c+1}/7]: '))
    if valor % 2 == 0:
        todosvalores[0].insert(c, valor)
    else:
        todosvalores[1].insert(c, valor)
   # todosvalores.append(valor)
todosvalores[0].sort()
todosvalores[1].sort()
print(f'Os valores pares digitados foram: {todosvalores[0]}')
print(f'Os valores ímpares digitados foram: {todosvalores[1]}')
#print(todosvalores[1])

