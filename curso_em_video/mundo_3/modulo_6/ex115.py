from mundo_3.modulo_6.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:

    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        leia_arquivo(arq)

    elif resposta == 2:
        cadastre_pessoa(arq)

    elif resposta == 3:
        head(f'Saindo do sistema... Até logo!')
        break

    else:
        head('\033[31mErro! Digite uma opção válida!\033[30m')

    sleep(1)
