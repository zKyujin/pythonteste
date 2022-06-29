import datetime


def voto(ano):
    """
    :param ano: É o ano de nascimento da pessoa
    :return:
    """
    idade = datetime.datetime.now().year - ano
    if idade >= 18:
        resp = 'VOTO OBRIGATÓRIO'
    if idade >= 70:
        resp = 'VOTO OPCIONAL'
    if idade >= 16 and idade < 18:
        resp = 'VOTO OPCIONAL'
    if idade < 16:
        resp = 'VOTO NEGADO'
    print(f'Com {idade} anos: {resp}')


ano = int(input('Em que ano você nasceu? '))
voto(ano)



