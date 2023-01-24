''') Desenvolver um algoritmo que efetue
a soma de todos os números ímpares que são múltiplos
de três e que se encontram no conjunto dos números
de 1 até 500.'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} números é igual a {}'.format(cont, soma))
