from time import sleep


def maior(* num):

    count = m = 0

    print('\033[1;30m-=' * 20)
    print('Analisando os valores passados...')
    sleep(1)

    for valor in num:

        print(f'{valor}', end=' ')
        sleep(0.3)

        if count == 0:
            m = valor
        else:
            if valor > m:
                m = valor

        count += 1

    print(f'\nForam informados {count} valores ao todo.'
          f'\nO maior valor informado foi: {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()
