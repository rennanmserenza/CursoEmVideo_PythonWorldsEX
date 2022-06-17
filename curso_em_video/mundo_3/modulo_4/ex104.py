def leiaint(num):

    ok = False
    valor = 0

    while True:

        n = input(num)

        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print('\033[31mERRO! Tente novamente digite apenas números inteiros.\033[30m')

        if ok:
            break

    return valor


# Programa Principal
entrada = leiaint('\n\033[1;30mDigite um número: ')
print(f'Você acabou de digitar o número {entrada}.')
