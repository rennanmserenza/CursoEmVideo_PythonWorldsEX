from random import randint

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(jogo da Adivinhação)===================================\033[m')

nr = randint(0, 5)
n = int(input('\n\033[1;30mDigite um número de 0 à 5: '))
print(f'\nO número que você escolheu foi \033[34m{n}\033[30m, o número sorteado foi \033[34m{nr}\033[30m.')
if (nr / n) == 1 or nr == n:
    print(f'Você acertou parabéns!!'
          f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
    print(f'Desculpe, não foi dessa vez tente novamente!'
          f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
