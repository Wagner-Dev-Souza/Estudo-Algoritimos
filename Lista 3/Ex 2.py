'''Desenvolver um algoritmo que leia a
altura de 15 pessoas. Este programa deverá calcular
e mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo;'''

maior = 0
menor = 0
for h in range(1, 16):
    altura = float(input('Altura da {}ª pessoa: '.format(h)))
    if h == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
print('A maior altura digitada foi {:.2f}m'.format(maior))
print('A menor altura digitada foi {:.2f}m'.format(menor))