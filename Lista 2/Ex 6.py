'''Escreva um algoritmo que lê dois valores
booleanos (lógicos) e então determina se ambos são
VERDADEIROS ou FALSOS.'''

A = bool(input('informe "V" ou "F" para o valor A: '))
B = bool(input('informe "V" ou "F" para o valor B: '))

if A == B:
    x = 'Verdadeiros'
elif A != B:
    x = 'Falsos'
print('Ambos os valores são {}'.format(x))
