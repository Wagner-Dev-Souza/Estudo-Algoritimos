'''Três amigos, Carlos, André e Felipe.
decidiram rachar igualmente a conta de um bar.
Faça um algoritmo para ler o valor total da conta e
imprimir quanto cada um deve pagar, mas faça com que
Carlos e André não paguem centavos.
Ex: uma conta de R$101,53 resulta em R$33,00 para
Carlos, R$33,00 para André e R$35,53 para Felipe.'''

conta = float(input('Insira o valor total da conta: R$ '))
d = conta // 3
f = conta - d * 2
print('Carlos e André pagarão R$ {:.2f}  e Felipe pagará R$ {:.2f}'.format(d, f))