'''Faça um algoritmo que leia os valores
A, B, C e imprima na tela se a soma de A + B
é menor que C.'''

A = float(input('Digite um valor para A: '))
B = float(input('Digite um valor para B: '))
C = float(input('Digite um valor para C: '))
soma = A + B

if soma >= C:
    print('Soma de A + B NÃO é menor que C')
else:
    print('Soma de A + B é menor que C')
