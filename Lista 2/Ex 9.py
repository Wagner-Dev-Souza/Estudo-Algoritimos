'''Tendo como dados de entrada a altura
e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes
fórmulas:
● para homens: (72.7 * h) – 58;
● para mulheres: (62.1 * h) – 44.7.'''

h = float(input('Digite sua altura: '))
s = str(input('Digite seu sexo: ').lower())
if s == 'masculino':
    p = (72.7 * h) - 58
elif s == 'feminino':
    p = (62.1 * h) - 44.7
else:
    print('valor incorreto. Tente novamente...')
print('Seu peso ideal é {:.2f}'.format(p))