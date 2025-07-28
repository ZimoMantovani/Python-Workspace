# 6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

data_inserida = input('Insira uma data valida (ex:DD/MM/AAAA): ')

if '/' not in data_inserida or len(data_inserida.split('/')) != 3:
    print('ERRO: Não foi possível completar a solicitação')
    exit()
    
data_separada = data_inserida.split('/')

print(data_separada)

dia = int(data_separada[0])
mes = int(data_separada[1])
ano = int(data_separada[2])

if dia > 31 or dia < 1:
    print('Dia invalido')
elif mes > 12 or mes < 1:
    print('Mês invalido')
elif ano > 2025:
    print('Ano invalido')
else:
    print('A data é valida')