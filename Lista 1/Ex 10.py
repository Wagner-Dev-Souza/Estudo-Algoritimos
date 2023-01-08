'''Construa um algoritmo para calcular a
distância entre dois pontos do plano cartesiano. Cada
ponto é um par ordenado (x,y).'''

from math import sqrt

xA = float(input('Insira o eixo x do ponto A: '))
yA = float(input('Insira o eixo y do ponto A: '))
xB = float(input('Insira o eixo x do ponto B: '))
yB = float(input('Insira o eixo y do ponto B: '))

d2 = (xB - xA)**2 + (xB - xA)**2
d = sqrt(d2)

print('A distância entre os dois pontos é {:.3f}'.format(d))
