'''Faça um algoritmo que receba o ano de
nascimento de uma pessoa e o ano atual, calcule e
mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.'''



an = int(input('Digite o ano do seu nascimento: '))
aa = int(input('Digite o ano atual: '))
a = aa - an
b = a * 12
c = a * 365
d = c / 7

print('Você tem {} anos,\n'
      'que equivalem a {} meses,\n'
      'ou {} dias,\n'
      'ou ainda {:.0f} semanas.'.format(a, b, c, d))

