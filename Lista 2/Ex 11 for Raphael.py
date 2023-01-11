'''Elabore um algoritmo que calcule o
que deve ser pago por um produto, considerando o
preço normal de etiqueta e a escolha da condição de
pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e
efetuar o cálculo adequado.
Faz o seguinte...
1 À vista com 10% de desconto!
2 Em 2x - x% de juros
3 Até 5x - 2X% de juros
4 Até  10x - 3X% de juros'''

preco = float(input('Informe o valor do produto: R$ '))
print('''Escolha a condição de pagamento:
[ 1 ] À vista com 10% de desconto!!!
[ 2 ] Parcelado com juros...''')
opção = int(input('Opção: '))
if opção == 1:
    pag = preco - preco * 10 / 100

elif opção == 2:
    j = int(input('informe o juros (%): '))
    x = int(input('Quantas parcelas? '))
    if x == 2:
        pag = preco + preco * j / 100
        print('Você pagará em 2x de R$ {:.2f}.'.format(pag / 2))
    elif x > 2 and x <= 5:
        pag = preco + preco * (j * 2) /100
        print('Você pagará em {}x de R$ {:.2f}.'.format(x, pag / x))
    elif x > 5 and x <= 10:
        pag = preco + preco * (j * 3) / 100
        print('Você pagará em {}x de R$ {:.2f}.'.format(x, pag / x))
    else:
        pag = preco
        print('\33[31mOpção Invalida. Tente novamente...\33[m')

else:
    pag = preco
    print('\33[31mOpção Invalida. Tente novamente...\33[m')
print('O valor do seu produto é de {:.2f} e você irá pagar {:.2f}'.format(preco, pag))

