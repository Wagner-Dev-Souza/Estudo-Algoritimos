'''Ler um número inteiro (assuma até três
dígitos) e imprimir a saída da seguinte forma:
CENTENA = x
DEZENA = x
UNIDADE = x'''

n = int(input('Insira um número de até 3 dígitos: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10

print('Analizando o número \33[33m{}\33[m'.format(n))
print('Centena: \33[35m{}\33[m\n'
      'Dezena: \33[36m{}\33[m\n'
      'Unidade: \33[34m{}\33[m\n'.format(cen, dez, uni))
