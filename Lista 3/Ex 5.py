'''Faça um algoritmo estruturado que leia
uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a
média de valores pares e a média geral dos números
lidos. O número que encerrará a leitura será zero.'''

print('Digite números positivos')

num = par = impar = mediap = media = soma = somap = cont = 0
while num >= 0:
    num = float(input('Digite um número [0 para encerrar]: '))
    soma += num

    if num <= 0:
        break
    if num % 2 == 0:
        somap += num
        par += 1
    else:
        impar +=1
if soma != 0:
    media = soma / (par + impar)

    if par == 0:
        mediap = 0
    else:
        mediap = somap / par
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
print('A média geral dos números foi de {:.2f}\n'
      'e a média dos números pares foi de {:.2f}'.format(media, mediap))