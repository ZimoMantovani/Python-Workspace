# 8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = int(input('Digite um numero inteiro: '))

resto = num % 2

if(resto == 1):
    print('Impar')
else:
    print('Par')