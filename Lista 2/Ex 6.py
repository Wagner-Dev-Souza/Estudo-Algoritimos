'''Escreva um algoritmo que lê dois valores
booleanos (lógicos) e então determina se ambos são
VERDADEIROS ou FALSOS.'''

print('Insira valores "V" ou "F"')
A = input('informe um valor A: ').upper()
B = input('informe um valor B: ').upper()

if A == 'F' and B == 'F':
    x = 'Falsos'
else:
    x = 'Verdadeiros'
print('Ambos os valores são {}'.format(x))
