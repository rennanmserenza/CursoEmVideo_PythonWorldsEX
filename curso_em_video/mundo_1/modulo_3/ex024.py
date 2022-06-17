print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=============(Verificando letras)===================================\033[m')

cidade = str(input('\n\033[1;30mDigite o nome de uma cidade: ')).strip()
c = cidade.lower().split()

print(f'No nome da cidade \033[32m{cidade.title()}\033[30m existe a palavra santo no começo? \033[34m{"santo" in c[0]}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
