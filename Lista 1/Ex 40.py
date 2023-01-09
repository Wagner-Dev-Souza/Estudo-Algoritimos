'''Faça um algoritmo que receba o valor
dos catetos de um triângulo, calcule e mostre o
valor da hipotenusa.'''


co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h2 = co**2 + ca**2
h = h2**(1/2)
print('Para os catetos {} e {} a hipotenusa é igual a {:.2f}'.format(co, ca, h))