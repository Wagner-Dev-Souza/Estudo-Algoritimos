'''Um motorista deseja colocar no seu
tanque X reais de gasolina. Escreva um algoritmo
para ler o preço do litro da gasolina e o valor
do pagamento, e exibir quantos litros ele conseguiu
colocar no tanque.'''

gas = float(input('Informe o valor do litro da gasolina: R$ '))
valor = float(input('Informe o valor pago: R$ '))
tanque = valor / gas

print('Com R$ {:.2f} é possivel abastecer {:.3f} litros de gasolina no tanque'.format(valor, tanque))