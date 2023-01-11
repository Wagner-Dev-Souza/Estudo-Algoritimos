''') Escreva um algoritmo que leia o número
de identificação, as 3 notas obtidas por um aluno
nas 3 verificações e a média dos exercícios que
fazem parte da avaliação, e calcule a média de
aproveitamento, usando a fórmula:
MA := (nota 1 + nota 2 * 2 + nota 3 * 3 + ME) / 7
A atribuição dos conceitos obedece a tabela abaixo.
O algoritmo deve escrever o número do aluno,
suas notas, a média dos exercícios,
a média de aproveitamento, o conceito
correspondente e a mensagem 'Aprovado' se o
conceito for A, B ou C, e 'Reprovado' se o
conceito for D ou E.
Média de aproveitamento Conceito
>= 90 A
>= 75 e < 90 B
>= 60 e < 75 C
>= 40 e < 60 D
< 40 E'''

print('UTILIZE APENAS NÚMEROS INTEIROS')
n = int(input('Informe o número de identificação do aluno: '))
n1 = int(input('Informe a nota da primeira verificação do aluno {}: '.format(n)))
n2 = int(input('Informe a nota da segunda verificação do aluno {}: '.format(n)))
n3 = int(input('Informe a nota da terceira verificação do aluno {}: '.format(n)))
me = int(input('informe a média dos exercícios do aluno {}: '.format(n)))
ma = (n1 + n2 * 2 + n3 * 3 + me) / 7

if ma >= 90:
    conceito = 'A'
elif ma >= 75:
    conceito = 'B'
elif ma >= 60:
    conceito = 'C'
elif ma >= 40:
    conceito = 'D'
else:
    conceito = 'E'

print('O aluno {} recebeu notas {}, {} e {} nas verificações\n'
      'e sua média nos exercícios foi {}, assim,\n'
      'sua média de aproveitamento foi {:.2f}.'.format(n, n1, n2, n3, me, ma))
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    resume = '\33[32mAPROVADO, PARABENS!!!\33[m'
    print('Tendo conceito {} o aluno {} está\n'
          '{}'.format(conceito, n, resume))
else:
    resume = '\33[31mREPROVADO, ESTUDE MAIS...\33[m'
    print('Tendo conceito {} o aluno {} está\n'
          '{}'.format(conceito, n, resume))