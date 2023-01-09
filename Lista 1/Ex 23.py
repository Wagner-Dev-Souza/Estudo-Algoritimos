'''Num dia de sol, você deseja medir a
altura de um prédio, porém, a trena não é
suficientemente longa. Assumindo que seja possível
medir sua sombra e a do prédio no chão, e que você
lembre da sua altura, faça um algoritmo para ler
os dados necessários e calcular a altura do prédio.'''

altura = float(input('Informe sua altura em M: '))
S = float(input('Informe a medida da sua sombra: '))
Sp = float(input('Informe a medida da sombra do prédio: '))

P = altura * Sp / S

print('A altura do prédio é de {:.3f} metros'.format(P))
