n = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n
if n2 > n and n2 > n3:
    maior = n2
if n3 > n and n3 >n2:
    maior = n3
menor = n
if n2 < n and n2 < n3:
    menor = n2
if n3 < n and n3 < n2:
    menor = n3
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')



#if n > n2 and n > n3:
    #m1 = n
   # print(f'O maior valor é {m1}')
#if n2 > n and n2 > n3:
   # m1 = n2
   # print(f'O maior valor é {m1}')
#if n3 > n and n3 > n2:
   # m1 = n3
    #print(f'O maior valor é {m1}')

