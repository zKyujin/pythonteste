palavras =('açai', 'pao', 'almoço', 'louça', 'programção', 'doideira', 'eosguri')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letras in p:
        if letras.lower() in "aeiou":
            print(letras, end='')
