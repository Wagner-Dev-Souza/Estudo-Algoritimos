'''Uma confecção produz X blusas de lã e
para isto gasta uma certa quantidade de novelos. Faça
um algoritmo para calcular quantos novelos de lã ela
gasta por blusa.'''

x = int(input("informe o número de blusas: "))
n = int(input("informe o número de novelos gastos: "))
l = n / x

print('Ela gasta {:.4f} novelos de lã por blusa...'.format(l))

