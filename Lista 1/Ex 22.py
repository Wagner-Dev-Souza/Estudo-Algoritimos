'''Pedrinho tem um cofrinho com muitas
moedas, e deseja saber quantos reais conseguiu
poupar. Faça um algoritmo para ler a quantidade de
cada tipo de moeda, e imprimir o valor total
economizado, em reais. Considere que existam moedas
de 1, 5, 10, 25 e 50 centavos, e ainda moedas de
1 real. Não havendo moeda de um tipo, a quantidade
respectiva é zero.'''

uc = int(input('Quantas moedas de 1 centavo existem? '))
cc = int(input('Quantas moedas de 5 centavo existem? '))
dc = int(input('Quantas moedas de 10 centavo existem? '))
vc = int(input('Quantas moedas de 25 centavo existem? '))
m = int(input('Quantas moedas de 50 centavo existem? '))
r = int(input('Quantas moedas de 1 real existem? '))
total = uc * 0.01 + cc * 0.05 + dc * 0.10 + vc * 0.25 + m * 0.50 + r * 1.00

print('O valor total é de R$ {:.2f}'.format(total))