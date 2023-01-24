'''Escrever um algoritmo que leia uma
quantidade desconhecida de números e conte quantos
deles estão nos seguintes intervalos: [0-25],
[26-50], [51-75] e [76-100]. A entrada de dados
deve terminar quando for lido um número negativo.'''

num = cont = cont1 = cont2 = cont3 = cont4 = 0
while num >= 0:
    num = int(input('Digite um número: '))
    cont += 1
    if num >= 0 and num < 26:
        cont1 += 1
    elif num >= 26 and num < 51:
        cont2 += 1
    elif num >=51 and num < 76:
        cont3 += 1
    elif num >= 76 and num < 101:
        cont4 += 1
print('Você digitou {} números\n'
      '{} entre 0-25\n'
      '{} entre 26-50\n'
      '{} entre 51-75\n'
      '{} entre 76-100'.format(cont, cont1, cont2, cont3, cont4))