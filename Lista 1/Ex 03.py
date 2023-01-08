'''A padaria Hotpão vende uma certa
quantidade de pães franceses e uma quantidade
de broas a cada dia. Cada pãozinho custa R$ 0,12
e a broa custa R$ 1,50. Ao final do dia, o dono quer
saber quanto arrecadou com a venda dos pães e broas
(juntos), e quanto deve guardar numa conta de
poupança (10% do total arrecadado).
Você foi contratado para fazer os cálculos para o
dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular
os dados solicitados.'''

P = int(input('Insira o número de pães vendidos: '))
B = int(input('Insira o número de broas vendidas: '))
Vp = 0.12 * P
Vb = 1.50 * B

print('O valor total arrecadado foi de \33[32mR$ {:.2f}\33[m\n'
      'e o valor que deve ser guardado na poupança é de \33[33mR$ {:.2f}\33[m'.format(Vb + Vp, (Vb + Vp) * 10 / 100))

