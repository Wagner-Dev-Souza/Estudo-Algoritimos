'''Desenvolver um algoritmo que leia um
número não determinado de valores e calcule e
escreva a média aritmética dos valores lidos,
a quantidade de valores positivos,
a quantidade de valores negativos e o percentual de
valores negativos e positivos.'''

resp = 'S'
soma = cont = media = pos = neg = perc_p = perc_n = 0
while resp in 'Ss':
    núm = float(input('Digite um número: '))
    soma += núm
    cont += 1
    if núm < 0:
        neg += 1
    else:
        pos += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
perc_p = (pos / cont) * 100
perc_n = (neg / cont) * 100
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('{} valores foram positivos e {} foram negativos.'.format(pos, neg))
print('O percentual de valores positivos foi de {:.2f}%\n'
      'e negativo foi de {:.2f}%'.format(perc_p, perc_n))
