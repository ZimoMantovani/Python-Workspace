# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.
temp = 0
cont = 0
totalTemp = 0
while temp >= -273.0:
    temp = float(input('Escreva uma temperatura em Celcius(para encerrar digite -273): '))
    if(temp >= -273.0):
        break
    
    totalTemp += temp
    cont += 1

print(f'A soma das temperaturas foi de {totalTemp} / {cont} = {totalTemp/cont}')
