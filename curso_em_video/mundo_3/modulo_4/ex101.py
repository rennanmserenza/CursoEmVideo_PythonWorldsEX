def voto(ano=18):

    from datetime import date

    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos, o voto é: NEGADO!'
    elif 16 >= idade < 18 or idade >= 65:
        return f'Com {idade} anos, o voto é: OPCIONAL!'
    else:
        return f'Com {idade} anos, o voto é: OBRIGATÓRIO!'


print('\033[1;30m-' * 30)
a = int(input('Em que ano você nasceu? '))
print(voto(a))
