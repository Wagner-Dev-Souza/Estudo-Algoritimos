'''Alguns países medem temperaturas em graus
Celsius, e outros em graus Fahrenheit. Faça um
algoritmo para ler uma temperatura Celsius e
imprimi-la em Fahrenheit (pesquise como fazer este
tipo de conversão).'''

C = float(input('Informe a temperatura em ºC: '))
F = C * 1.8 + 32
print('A temperatura de \33[36m{}ºC\33[m corresponde a \33[35m{}ºF\33[m!'.format(C, F))
