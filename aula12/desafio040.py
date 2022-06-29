n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi de {media}. Portanto, você foi \033[31mREPROVADO!\033[m')
if media >= 5 and media <= 6.9:
    print(f'Sua média foi de {media}. Portanto, você está de \033[33mRECUPERAÇÃO\033[m!')
if media >= 7:
    print(f"Sua média foi de {media}. Portanto, você foi \033[34mAPROVADO\033[m! Parabéns!")