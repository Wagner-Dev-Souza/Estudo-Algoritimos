'''Encontrar o dobro de um número caso
ele seja positivo e o seu triplo caso seja negativo,
imprimindo o resultado.'''

n = float(input('Digite um número positivo ou negativo: '))
if n > 0:
    print('O dobro desse número é {:.2f}'.format(n * 2))
else:
    print('O triplo desse número é {:.2f}'. format(n * 3))