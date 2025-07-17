#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

num = input('Digite um numero (inteiro ou decimal): ')

if ('.' in num or ',' in num):
    print('Decimal')
else:
    print('Inteiro')
