from time import sleep

c = ('\033[m',          # 0 -> Cor: Sem Cores
     '\033[1;30;41m',   # 1 -> Cor: Vermelho
     '\033[1;30;42m',   # 2 -> Cor: Verde
     '\033[1;30;43m',   # 3 -> Cor: Amarelo
     '\033[1;30;44m',   # 4 -> Cor: Azul
     '\033[1;30;45m',   # 5 -> Cor: Roxo
     '\033[7;30m',      # 6 -> Cor: Branco
     )


def ajuda(cmd):

    titulo(f'Acessando o Manual do Comando/Biblíoteca {cmd}', 4)

    print(c[6], end='')
    help(cmd)
    print(c[0], end='')
    sleep(1)


def titulo(cmd, cor=0):
    tam = len(cmd) + 4

    print(c[cor], end='')
    print('~' * tam)
    print(f'  {cmd}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)


while True:

    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou Biblíoteca > '))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)
