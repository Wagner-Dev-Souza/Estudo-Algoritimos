'''Faça um algoritmo que leia uma variável
e some 5 caso seja par ou some 8 caso seja ímpar,
imprimir o resultado desta operação.'''

n = float(input('Digite um número: '))
x = n % 2
if x == 0:
    print('{:.2f}'.format(n + 5))
else:
    print('{:.2f}'.format(n + 8))