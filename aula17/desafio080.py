valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        p = 0
        while p < len(valores):
            if n <= valores[p]:
                valores.insert(p, n)
                break
            p += 1

print(valores)
