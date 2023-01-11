'''Escreva um algoritmo que leia três
valores inteiros e diferentes e mostre-os em ordem
decrescente.'''

print('Insira três valores inteiros diferentes:')
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))

if a > b > c:
    print(a, b, c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > b > a:
    print(c, b, a)
elif c > a > b:
    print(c, a, b)