def notas(*a, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param a: uma ou mais notas dos alunos.
    :param sit: situação dos alunos, baseada na média da sala.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = dict()
    dicio['total'] = len(a)
    dicio['maior'] = max(a)
    dicio['menor'] = min(a)
    dicio['média'] = sum(a) / len(a)
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio ['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio



# Programa Principal
resp = notas(5.5, 9.5, 1, 0.5, sit=True)
print(resp)
help(notas)
