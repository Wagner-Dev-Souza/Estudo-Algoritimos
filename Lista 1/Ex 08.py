'''Faça um algoritmo para ler três notas de
um aluno em uma disciplina e imprimir a sua média
ponderada (as notas tem pesos respectivos de 1, 2 e 3).'''

n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2: '))
n3 = float(input('Insira a nota 3: '))

mp = (n1 + n2 * 2 + n3 * 3) / 6

print('\33[33mA média ponderade desse aluno foi de\33[m', mp)