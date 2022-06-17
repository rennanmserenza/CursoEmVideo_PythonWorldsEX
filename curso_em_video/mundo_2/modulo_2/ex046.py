print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Contagem Regressiva)":=^138}\033[m\n')

from datetime import date
from time import sleep
import emojis

ano = date.today().year

for t in range(10, 0, -1):
      print(f'\033[1;30m{t}. ', end='')
      sleep(1)
print(emojis.encode(f'\nFeliz ano novo!! Que o seu \033[35m{ano}\033[30m seja maravilhoso. :tada: :balloon:'
                    f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m'))
