'''Faça um algoritmo que leia o nome, o
sexo e o estado civil de uma pessoa.
Caso sexo seja “F” e estado civil seja “CASADA”,
solicitar o tempo de casada (anos).'''

nome = str(input('Digite seu nome: '))
print('''Selecione o sexo:
 [ F ] Feminino
 [ M ] Masculino''')
sexo = str(input().upper())
estCiv = str(input('Informe o estado civil: ').lower())
if sexo == 'F' and estCiv == 'casada':
    tempo = int(input('Digite o tempo de casada em anos: '))


print(sexo)