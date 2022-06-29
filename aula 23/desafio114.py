import requests
try:
    resposta = requests.get('http://pudim.com.br')
except requests.ConnectionError:
    print('\033[1;31mO site pudim não está acessível por erro de conexão!\033[m')
except requests.Response:
    print('\033[31mNão obtive resposta do site Pudim! :(\033[m')
else:
        print('\033[1;33mConsegui acessar o site do Pudim com sucesso!\033[m')


