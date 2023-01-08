''' A imobiliária Imóbilis vende apenas
terrenos retangulares. Faça um algoritmo para ler
as dimensões de um terreno e depois exibir
a área do terreno.'''

n1 = float(input('Insira o comprimento do terreno em metros: '))
n2 = float(input('Insira a largura do terreno em metros: '))

print('A área deste terreno é de \33[31m{:.2f}\33[m metros²'.format(n1 * n2))
