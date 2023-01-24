'''Escreva um algoritmo que leia um valor
inicial A e imprima a seqüência de valores do
cálculo de A! e o seu resultado.
Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))