'''Um funcionário recebe um salário fixo
mais 4% de comissão sobre as vendas. Faça um
algoritmo que receba o salário fixo de um
funcionário e o valor de suas vendas, calcule e
mostre a comissão e o salário final do funcionário.'''

s = float(input('Informe o salário do funcionário: R$ '))
v = float(input('Informe o valor das vendas do funcionário: R$ '))
c = v * 4 / 100

print('A comissão do funcionario é de R$ {:.2f}\n'
      'e seu salário final totaliza R$ {:.2f}'.format(c, s + c))
