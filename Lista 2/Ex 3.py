'''Faça um algoritmo para receber um número
qualquer e informar na tela se é par ou ímpar'''


n = float(input('Digite um número: '))
x = n % 2

if x == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')
