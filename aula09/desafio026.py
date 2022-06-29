frase = str(input('Digite uma frase: '))
print(f'A letra "a" aparece {frase.lower().count("a")} vezes nessa frase.')
print(f'A letra "a" aparece na posição {frase.lower().find("a")} pela primeira vez')
print(f'A letra "a" aparece na posição {frase.lower().rfind("a") - frase.count(" ")} pela última vez')


