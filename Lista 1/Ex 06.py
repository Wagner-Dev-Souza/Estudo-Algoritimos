'''O restaurante a quilo Bem-Bão cobra
R$12,00 por cada quilo de refeição.
Escreva um algoritmo que leia o peso do prato
montado pelo cliente (em quilos) e imprima o valor a
pagar. Assuma que a balança já desconte o peso do prato.'''

n = float(input('Informe o peso do prato em kg: '))
preco = n * 12

print('O valor total a pagar é de \33[35mR$ {:.2f}'.format(preco))