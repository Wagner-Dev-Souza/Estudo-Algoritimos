'''Uma fábrica controla o tempo de trabalho
sem acidentes pela quantidade de dias.
Faça um algoritmo para converter este tempo em anos,
meses e dias. Assuma que cada mês possui sempre 30 dias.'''

dias = int(input('Informe o número de dias: '))
anos = dias // 365
dias = dias % 365
meses = dias // 30
dias = dias % 30
print('O tempo de trabalho sem acidentes é de \33[35m{}\33[m anos, \33[35m{}\33[m meses e \33[35m{}\33[m dias'. format(anos, meses, dias))