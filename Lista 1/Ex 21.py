'''A fábrica de refrigerantes Meia-Cola
vende seu produto em três formatos: lata de 350 ml,
garrafa de 600 ml e garrafa de 2 litros. Se um
comerciante compra uma determinada quantidade de
cada formato, faça um algoritmo para calcular
quantos litros de refrigerante ele comprou.'''

l = int(input('Digite o número de latas de 350ml: '))
gp = int(input('Digite o número de garrafas de 600ml: '))
gg = int(input('Digite o número de garrafas de 2L: '))
t = l * 0.350 + gp * 0.6000 + gg * 2.000

print('O comerciante comprou um total de {:.3f} litros de refrigerante'.format(t))
