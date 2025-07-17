# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if(numero1 > numero2):
    print(f'O maior numero é o {numero1}')
elif(numero1 < numero2):
    print(f'O maior numero é o {numero2}')
else:
    print('Os numeros são os mesmos.')
