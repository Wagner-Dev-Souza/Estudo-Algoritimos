''' Faça um algoritmo para calcular quantas
ferraduras são necessárias para equipar todos os
cavalos comprados para um haras.'''

cavalos = int(input('Insira o número de cavalos: '))

F = cavalos * 4

print('\33[33mSerão necessárias \33[32m{}\33[33m ferraduras para equipar \33[32m{}\33[33m cavalos'.format(F, cavalos))