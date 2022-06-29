from UtilidadesCeV.moeda import resumo
from UtilidadesCeV.dado import leiadinheiro

#p = float(input('Digite um preço: R$'))
#moeda.resumo(p, 80, 35)


p = leiadinheiro(('Digite um preço: R$'))
resumo(p, 80, 35)
