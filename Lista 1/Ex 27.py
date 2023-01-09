'''Faça um algoritmo que receba dois
números, calcule e mostre a divisão do primeiro
número pelo segundo. Sabe-se que o segundo número
não pode ser zero, portanto não é necessário se
preocupar com validações.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

t = n1 / n2

print('A divisão de {} por {} é igual a: {}'.format(n1, n2, t))
