# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.


letra = input('Digite uma letra para verificar se é vogal ou consoante:')

if letra.lower() not in 'aeiou':
    print('consoante')
else: 
    print('vogal')
