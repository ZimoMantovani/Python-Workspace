#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária 
# qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número 
# - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

op = int(input('Qual operação deseja realizar? \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n'))

if(op == 1):
    resultado = num1 + num2
elif(op == 2):
    resultado = num1 - num2
elif(op == 3):
    resultado = num1 * num2
elif(op == 4):
    resultado = num1 / num2
else:
    print('Digite um valor valido.')
#Mostra o resultado

print(f'Resultado: {resultado:.2f}')
    
    
#Verifica se é par ou impar
resto = resultado % 2
if(resto == 1):
    print('É impar')
else:
    print('É par')

#Verifica se é positivo ou negativo
if(resultado <0):
    print('O resultado é negativo')
else:
    print('O resultado é positivo')

#Verifica se é inteiro ou decimal

if float(resultado).is_integer():
    print('Inteiro')
else:
    print('Decimal')