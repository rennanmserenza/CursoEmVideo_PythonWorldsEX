def notas(* n, sit=False):

    """
    ->Função para analisar notas e a situação de vários alunos.
    :param n: uma ou mais notas dos alunos(aceita várias notas.)
    :param sit: valor opcional, indicando se deve ou não, adicionar a situação da turma.
    :return: dicionário com várias informações sobre a situação dos alunos da turma.
    """

    nota = dict()

    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['media'] = sum(n) / len(n)

    if sit:

        if nota['media'] >= 7.0:
            nota['situação'] = 'Boa'

        elif nota['media'] >= 5.0:
            nota['situação'] = 'Razoável'

        else:
            nota['situação'] = 'Ruim'

    return nota


# Programa Principal
resp = notas(5.0, 7.2, 3.6, 9.1, 7.8, sit=True)
print(resp)
