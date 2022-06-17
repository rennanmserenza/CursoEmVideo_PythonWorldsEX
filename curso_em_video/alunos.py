alunos = list()

pergunta = list()
respostas = list()

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

maior = menor = media = 0

while True:
    count = 0

    nome = (str(input('\nDigite o nome do aluno: ')).strip().title())
    respostas.append(nome)

    for x in range(0, 10):
        y = str(input(f'Digite a resposta da pergunta nº{x + 1:^3}(A, B, C, D, E): ' if x != 10
                      else f'Digite a resposta da pergunta nº{x + 1:^4}(A, B, C, D, E): ')).strip().upper()[0]
        pergunta.append(y)

        if gabarito[x] == y:
            count += 1

    respostas.append(pergunta[:])
    respostas.append(count)
    alunos.append(respostas[:])
    pergunta.clear()
    respostas.clear()

    r = str(input('Gostaria de cadastrar a nota de mais algum aluno[S/N]? ')).strip().upper()[0]

    if r == 'N':
        break

for pos, n in enumerate(alunos):
    if pos == 0:
        maior = menor = n[2]
    elif n[2] > maior:
        maior = n[2]
    elif n[2] < menor:
        menor = n[2]
    media += n[2]

media_aluno = media / len(alunos)

print(len(alunos), maior, menor, media_aluno)
