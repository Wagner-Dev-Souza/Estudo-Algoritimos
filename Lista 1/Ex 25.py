'''Calcule o volume de uma caixa d'água
cilíndrica.'''

h = float(input("Insira a altura da caixa d' em M: "))
r = float(input("Insira o raio da caixa d'água em M: "))
v = 3.14 * (r ** 2) * h

print("O volume da caixa d'agua é de {} m³.".format(v))