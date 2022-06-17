from mundo_3.modulo_6.ex113.utilidadesCeV.dado import *

p = leia_int('\n\033[1;30mNumerador: ')
q = leia_float(f'Denominador: ')
print(f'\nO número inteiro foi: {p}.'
      f'\nO número real digitado foi: {q.replace(".", ",")}.')
