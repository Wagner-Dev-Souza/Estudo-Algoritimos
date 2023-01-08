'''Entrar com o dia e o mês de uma data e
informar quantos dias se passaram desde o início do
ano. Esqueça a questão dos anos bissextos e
considere sempre que um mês possui 30 dias.'''

d = int(input('Insira o dia: '))
m = int(input('Insira o mês: '))
tempo = (m-1) * 30 + d

print('Já se passaram \33[34m{}\33[m dias desde o início do ano.'.format(tempo))