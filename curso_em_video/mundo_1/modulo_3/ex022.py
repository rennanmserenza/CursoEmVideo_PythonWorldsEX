from time import sleep
print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Analizador de texto)===================================\033[m')

n = str(input('\n\033[1;30mDigite seu nome completo: ')).strip().title()
M = n.upper()
m = n.lower()
c = ''.join(n.split())
cf = n.capitalize().split()

print(f'\nANALISANDO SEU NOME...')
sleep(3)

print(f'\nSeu nome todo MAIUSCULO: \033[33m{M}\033[30m.'
      f'\nSeu nome todo MINUSCULO: \033[33m{m}\033[30m.'
      f'\nSeu nome tem ao todo: \033[35m{len(c)}\033[30m letras.'
      f'\nSeu primeiro nome é \033[33m{cf[0]}\033[30m e ele tem \033[35m{len(cf[0])}\033[30m letras.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
