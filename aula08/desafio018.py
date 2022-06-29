import math
an = int(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'seno: {seno:.2f}º \n cosseno: {cosseno:.2f}º \n tangente: {tangente:.2f}º ')
