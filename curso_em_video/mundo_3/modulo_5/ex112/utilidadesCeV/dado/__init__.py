def leia_dinheiro(txt):

    while True:

        entrada = str(input(txt)).strip().replace(',', '.')

        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido!\033[30m')

        else:
            break

    return float(entrada)
