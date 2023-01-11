'''Elabore um algoritmo que calcule o
que deve ser pago por um produto, considerando o
preço normal de etiqueta e a escolha da condição de
pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e
efetuar o cálculo adequado.
Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em duas vezes, preço normal de etiqueta mais juros de 10%'''

preco = float(input('Informe o valor do produto: R$ '))
print('''Escolha a condição de pagamento:
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais vezes''')
opção = int(input('Opção: '))
if opção == 1:
    pag = preco - preco * 10 / 100
    print('')
elif opção == 2:
    pag = preco - preco * 15 / 100
elif opção == 3:
    pag = preco
    print('Você pagará em 2x de R$ {:.2f}.'.format(pag / 2))
elif opção == 4:
    x = int(input('Quantas parcelas? '))
    pag = preco + preco * 10 / 100
    print('Você pagará em {}x de R$ {:.2f}'.format(x, pag / x))
else:
    pag = preco
    print('Opção Invalida. Tente novamente...')
print('O valor do seu produto é de {:.2f} e você irá pagar {:.2f}'.format(preco, pag))

