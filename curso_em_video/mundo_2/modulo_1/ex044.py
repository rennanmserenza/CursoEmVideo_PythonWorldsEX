print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Gerenciador de Pagamentos)":=^138}\033[m')

n = input('\n\033[1;30mOlá seja bem vindo! Qual é o seu nome? ').lower().title().strip()
print(f'\nOlá, \033[34m{n}\033[30m!')
v = float(input(f'Digite o valor da compra: '))
p = int(input(f'Escolha a forma de pagamento?'
              f'\n\033[35m1)\033[30m À vista em dinheiro.       \033[35m2)\033[30m À vista no cartão.'
              f'\n\033[35m3)\033[30m Em até 2x cartão.          \033[35m4)\033[30m Em 3x ou mais no cartão.'
              f'\nSua escolha: '))

if p == 1:
      print(f'\n\033[34m{n}\033[30m você escolheu como forma de pagamento o modo \033[33mà vista e em dinheiro\033[30m.'
            f'\nVocê recebeuu \033[34m10% de desconto\033[30m na sua compra. Compra: R$\033[35m{v * 0.9:.2f}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif p == 2:
      print(f'\n\033[34m{n}\033[30m você escolheu como forma de pagamento o modo \033[33mà vista e em cartão\033[30m.'
            f'\nVocê recebeuu \033[34m5% de desconto\033[30m na sua compra. Compra: R$\033[35m{v * 0.95:.2f}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif p == 3:
      print(f'\n\033[34m{n}\033[30m você escolheu como forma de pagamento o modo \033[33mparcelado em até 2x no cartão\033[30m.'
            f'\nCompra: R$\033[35m{v:.2f}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif p == 4:
      print(f'\n\033[34m{n}\033[30m você escolheu como forma de pagamento o modo \033[33mparcelado em 3x ou mais no cartão\033[30m.'
            f'\nCompra: R$\033[35m{v * 1.2:.2f}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print(f'comando inválido, reinicie o programa e tente novamente.')
