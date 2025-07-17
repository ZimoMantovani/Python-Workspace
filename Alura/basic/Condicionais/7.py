# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = int(input('Qual turno você trabalha? \n 1 - Manhã \n 2 - Tarde \n 3 - Noite\n'))


if(turno == 1):
    print('Bom dia!')
elif(turno == 2):
    print("Boa tarde!")
elif(turno == 3):
    print('Boa noite!')
else:
    print('Valor invalido')
