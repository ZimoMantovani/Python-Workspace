#8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência.
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e 
# mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100].
# Encerre a entrada de dados com um número negativo.
faixa = {
    '0-25':0,
    '26-50':0,
    '51-75':0,
    '76-100':0,
}
print(type(faixa))
cont = 0
while True:
    idade = int(input('Escreva uma idade(Encerre com uma idade negativa): '))
    if idade < 0:
        break
    if 0 <= idade <= 25:
        faixa['0-25'] += 1
    elif 26 <= idade <= 50:
        faixa['26-50'] += 1
    elif 51 <= idade <= 75:
        faixa['51-75'] += 1
    elif 76 <= idade <= 100:
        faixa['76-100'] += 1
    cont += 1
print(f"Entre 0-25: {faixa['0-25']}")
print(f"Entre 26-50: {faixa['26-50']}")
print(f"Entre 51-75: {faixa['51-75']}")
print(f"Entre 76-100: {faixa['76-100']}")