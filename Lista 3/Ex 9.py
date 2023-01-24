'''Escreva um algoritmo que leia um valor
inicial A e uma razão R e imprima uma seqüência em
P.G. contendo 10 valores.'''

A = int(input('Primeiro termo: '))
R = int(input('Razão: '))
termo = A
cont = 1
while cont <=10:
    print('{} -> '.format(termo), end="")
    termo *= R
    cont += 1
print('Fim')