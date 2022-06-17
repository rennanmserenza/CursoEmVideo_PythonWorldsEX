def leia_int(num):

    valor = 0

    while True:

        try:
            n = input(num)

        except (ValueError, TypeError):
            print(f'\033[31mTivemos um problema com o tipo de dado que você inseriu.')
            continue

        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuário!')
            return 0

        else:
            if n.isnumeric():
                valor = int(n)
                break

            else:
                print('\033[31mERRO! Tente novamente digite apenas números inteiros.\033[30m')

    return valor


def leia_float(num):

    ok = False
    valor = 0

    while True:

        try:
            n = input(num)

        except(ValueError, TypeError):
            print(f'\033[31mTivemos um problema com o tipo de dado que você inseriu.')
            continue

        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuário!')
            return 0

        else:
            if n.isnumeric():
                valor = float(n)
                ok = True

            else:
                print('\033[31mERRO! Tente novamente digite apenas números inteiros.\033[30m')

            if ok:
                break

    return valor
