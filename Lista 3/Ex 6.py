'''Escrever um algoritmo que gera e
escreve os números ímpares entre 100 e 200'''

for c in range (100, 200):
    if c % 2 != 0:
        print(c, end='->')
print('Fim')