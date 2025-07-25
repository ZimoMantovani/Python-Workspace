# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
valor1= int(input('Escreva um valor inteiro: '))
valor2= int(input('Escreva outro valor inteiro: '))
valores = 0
for valores in range(valor1+1, valor2):
    print(valores)