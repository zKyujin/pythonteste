expressao = str(input('Digite a expressão: '))
parenteses = []
for simb in expressao:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if parenteses == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')



