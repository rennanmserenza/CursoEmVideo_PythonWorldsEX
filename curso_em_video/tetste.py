mes = [['Janeiro'], ['Fevereiro'], ['Março'], ['Abril'], ['Maio'], ['Junho'],
       ['Julho'], ['Agosto'], ['Setembro'], ['Outubro'], ['Novembro'], ['Dezembro']]

temperaturas = []

media = 0

print('\nDigite as Temperaturas correspondentes com o Mês!')

for x in mes:
    temp = int(input(f"Digite a temperatura média do mês de {x[0]}: "))
    media += temp
    temperaturas.append(temp)

media_ano = media/12

print(f'O mês com a maior média de temperatura foi: ', end='')

for pos, t in enumerate(temperaturas):
    count = 0
    if t > media_ano:
        print(f'{mes[pos]} e a temperatura foi {t}', end=', ' if pos != 12 else f'{mes[pos]}e a temperatura foi {t}.')
        count += 1
