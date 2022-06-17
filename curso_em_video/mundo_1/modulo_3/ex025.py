print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Verificando  letras)===================================\033[m')

nome = str(input('\n\033[1;30mDigite o seu nome completo: ')).strip().lower()

print(f'\nSeu nome é \033[34m{nome.title()}\033[30m. Que belo nome você tem!'
      f'\nSeu nome possui Silva nele? \033[33m{"silva" in nome}\033[30m'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
