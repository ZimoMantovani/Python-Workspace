'''
Um estabelecimento está vendendo combustíveis com descontos variados. 
Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. 
Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. 
O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e 
calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o 
valor de desconto resultante do cálculo.
'''

litros = float(input('Qual a quantidade de litros vendidos: '))
tipo = input('Qual o tipo do combustivel(E para etanol e D para diesel): ')

if('E' or 'e' in tipo):
    print('Tipo: Etanol')
    totalGasto = litros*1.70
    
    if(litros > 0 and litros <15):
        desconto = totalGasto*0.02
        
        print(f'Total: {totalGasto}')
        print(f'Total com desconto de 2%: {totalGasto - desconto}')
    elif(litros > 15 ):
        desconto = totalGasto*0.04
        
        print(f'Total: {totalGasto}')
        print(f'Total com desconto de 4%: {totalGasto - desconto}')
    else:
        print('ERRO: A quantidade não pode ser menor que zero')

elif('D' or 'd' in tipo):
    print('Tipo: Diesel')
    totalGasto = litros*2
    
    if(litros > 0 and litros <15):
        desconto = totalGasto*0.03
        
        print(f'Total: {totalGasto}')
        print(f'Total com desconto de 3%: {totalGasto - desconto}')
    elif(litros > 15):
        desconto = totalGasto*0.05
        
        print(f'Total: {totalGasto}')
        print(f'Total com desconto de 5%: {totalGasto - desconto}')
    else:
        print('ERRO: A quantidade não pode ser menor que zero')
    


