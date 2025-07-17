# 4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais 
# alto e mais baixo entre esses três anos.

valor1 = float(input('Digite o valor do carro 1:'))
valor2 = float(input('Digite o valor do carro 2:'))
valor3 = float(input('Digite o valor do carro 3:'))

if(valor1 > valor2 and valor1 > valor3):
    print(f'O carro mais caro é o 1 com o valor de {valor1}')
elif(valor2 >valor1 and valor2 > valor3):
    print(f'O carro mais caro é o 2 com o valor de {valor2}')
elif(valor3 >valor1 and valor3 > valor1):
    print(f'O carro mais caro é o 3 com o valor de {valor3}')

if(valor1 < valor2 and valor1 < valor3):
    print(f'O carro mais barato é o 1 com o valor de {valor1}')
elif(valor2 <valor1 and valor2 < valor3):
    print(f'O carro mais barato é o 2 com o valor de {valor2}')
elif(valor3 <valor1 and valor3 < valor1):
    print(f'O carro mais barato é o 3 com o valor de {valor3}')