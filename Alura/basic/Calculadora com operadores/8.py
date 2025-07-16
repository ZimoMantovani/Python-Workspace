#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da 
# divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
try:

    valor1 = float(input('Digite o numerador: '))
    valor2 = float(input('Digite o denominador (não deve ser 0): '))

    valorTotal = valor1 % valor2

    print('Divisão: %.2f ' %(valorTotal))
except ZeroDivisionError:
    print('Erro: denominador não pode ser 0')
