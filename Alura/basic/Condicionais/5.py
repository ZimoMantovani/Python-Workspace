# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

valor1 = float(input('Digite o valor 1:'))
valor2 = float(input('Digite o valor 2:'))
valor3 = float(input('Digite o valor 3:'))

if(valor1 < valor2 and valor1 < valor3):
    print(f'O produto mais barato é o 1 com o valor de {valor1}')
elif(valor2 <valor1 and valor2 < valor3):
    print(f'O produto mais barato é o 2 com o valor de {valor2}')
elif(valor3 <valor1 and valor3 < valor1):
    print(f'O produto mais barato é o 3 com o valor de {valor3}')