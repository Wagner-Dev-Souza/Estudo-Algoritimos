'''Um tonel de refresco é feito com 8
partes de água mineral e 2 partes de suco de
maracujá. Faça um algoritmo para calcular quantos
litros de água e de suco são necessários para se
fazer X litros de refresco (informados pelo usuário).
'''

n = float(input('Informe a quantidade "em litros" de refresco a ser produzida: '))
d = n / 10
a = d * 8
s = d * 2

print('Serão necessários para fazer {:.3f} litros de refresco\n'
      '{:.3f} litros de água e {:.3f} litros de suco de maracujá'.format(n, a, s))