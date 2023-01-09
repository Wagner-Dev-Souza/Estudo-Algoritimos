'''Faça um algoritmo que receba duas
notas, calcule e mostre a média ponderada dessas
notas, considerando peso 2 para a primeira nota e
peso 3 para a segunda nota.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 * 2 + n2 * 3) /5

print('A média ponderada dessas notas é', m)