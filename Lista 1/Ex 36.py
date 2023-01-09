'''Faça um algoritmo que receba o valor do
salário mínimo e o valor do salário de um
funcionário, calcule e mostre a quantidade de
salários mínimos que ganha esse funcionário.'''

sm = float(input('Informe o valor do salário mínimo: R$ '))
sf = float(input('Informe o valor do salário do funcionário: R$ '))
t = sf / sm

print('O funcionário recebe {:.2f} salários mínimos.'.format(t))
