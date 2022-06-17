print('\033[1;30;44m=========(Rennan Mendes - Soluções)==================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)=====================================\033[m'
      '\n\n\033[1;30;44m=======(Calcule quantos Litros de tinta você usará)==================\033[m')

h = float(input('\n\033[1;30mDigite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
a = h * l

print(f'\nSua Área é de \033[33m{a}\033[30m m², você precisará de \033[34m{(a * 2)}\033[30m litros de tinta!'
      '\n\n\033[1;30;44m=============(Programa Finalizado)===================================\033[m')
