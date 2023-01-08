'''A empresa Hipotheticus paga R$10,00 por
hora normal trabalhada, e R$15,00 por hora extra.
Faça um algoritmo para calcular e imprimir o
salário bruto e o salário líquido de um determinado
funcionário. Considere que o salário líquido é
igual ao salário bruto descontando-se 10% de
impostos.'''

s = float(input('Informe as horas normais trabalhadas: '))
s2 = float(input('Informe as horas extras trabalhadas: '))
v1 = s * 10
v2 = s2 * 15
t = v1 + v2
l = t - t * 10 / 100

print('\33[33mO salário bruto do funcionário é R$ {:.2f} e o salário líquido é R$ {:.2f}'.format(t, l))
