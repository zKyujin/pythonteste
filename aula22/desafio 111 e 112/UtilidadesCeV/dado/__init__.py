def leiadinheiro(p):
    valido = False
    while not valido:
        entrada = str(input(p)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
