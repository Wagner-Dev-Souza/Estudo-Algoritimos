'''João recebeu seu salário de R$ 1200,00
e precisa pagar duas contas (C1=R$ 200,00 e
C2=R$120,00) que estão atrasadas. Como as contas
estão atrasadas, João terá de pagar multa de
2% sobre cada conta. Faça um algoritmo que
calcule e mostre quanto restará do salário do João.'''

salário = 1200
c1 = 200 + 200 * 2 / 100
c2 = 120 + 120 * 2 / 100
total = salário - (c1 + c2)

print('João recebera um salário de R$ {:.2f}'.format(salário))
print('O valor total das contas de João com as multas é de R$ {:.2f}'.format(c1 + c2))
print('Restará R$ {:.2f} do salário de João.'.format(total))