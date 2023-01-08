'''Faça um algoritmo para ler o salário de
um funcionário e aumentá-lo em 15%. Após o aumento,
desconte 8% de impostos.
Imprima o salário inicial, o salário com o aumento e
o salário final.'''

s = float(input('Insira aqui seu salário: R$ '))
a = s + s * 15 / 100
i = a - a * 8 / 100

print('\33[4;33mSeu salário de R$ {:.2f}\n'
      '\33[4;32mapós o aumento foi para R$ {:.2f}\n'
      '\33[4;31me após o desconto dos impostos totalizou \33[1;31;42mR$ {:.2f}\33[m'.format(s, a, i))