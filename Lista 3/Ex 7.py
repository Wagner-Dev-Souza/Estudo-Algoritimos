'''Escrever um algoritmo que leia um valor
para uma variável N de 1 a 10 e calcule a tabuada
de N. Mostre a tabuada na forma: 0 x N = 0,
1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.'''

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))