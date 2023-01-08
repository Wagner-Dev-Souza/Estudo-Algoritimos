'''A lanchonete Gostosura vende apenas um
tipo de sanduíche, cujo recheio inclui duas fatias de
queijo, uma fatia de presunto e uma rodela de
hambúrguer. Sabendo que cada fatia de queijo ou
presunto pesa 50 gramas, e que a rodela de hambúrguer
pesa 100 gramas, faça um algoritmo em que o dono
forneça a quantidade de sanduíches a fazer, e a
máquina informe as quantidades (em quilos) de queijo,
presunto e carne necessários para compra.'''

x = int(input('Insira o número de sanduíches: '))
q = x * 0.050 * 2
p = 0.050 * x
h = 0.100 * x

print('Você precisará comprar, \33[33m{:.3f} Kg de queijo\33[m, \33[31m{:.3f} kg de presunto\33[m e\n'
      ' \33[36m{:.3f} kg de carne'.format(q, p, h))

