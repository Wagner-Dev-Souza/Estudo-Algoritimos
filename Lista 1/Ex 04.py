'''Escreva um algoritmo para ler o nome
e a idade de uma pessoa, e exibir quantos
dias de vida ela possui. Considere sempre anos
completos, e que um ano possui 365 dias. Ex: uma
pessoa com 19 anos possui 6935 dias de vida; veja
um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935
DIAS'''

n = str(input('Insira seu nome: '))
i = int(input('Informe sua idade: '))
dias = i * 365
print('\33[3;32m{}\33[3;38m, VOCÊ JA VIVEU \33[3;31m{}\33[3;38m DIAS.'.format(n.upper(), dias))