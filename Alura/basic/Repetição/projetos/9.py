#9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). 
# Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. 
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

pessoa = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0, # nulo
    '6':0 # branco
}
for i in range(0,20):
    voto = int(input('Digite seu voto: '))
    if voto == 1:
        pessoa['1'] += 1
    elif voto == 2:
        pessoa['2'] +=1
    elif voto == 3:
        pessoa['3'] +=1
    elif voto == 4:
        pessoa['4'] +=1
    elif voto == 5:
        pessoa['5'] +=1
    elif voto == 6:
        pessoa['6'] +=1

# Exibe o total de votos para cada candidato, nulos e brancos
print(f"Votos para o candidato 1: {pessoa['1']} votos ({(pessoa['1']/20)*100:.2f}%)")
print(f"Votos para o candidato 2: {pessoa['2']} votos ({(pessoa['2']/20)*100:.2f}%)")
print(f"Votos para o candidato 3: {pessoa['3']} votos ({(pessoa['3']/20)*100:.2f}%)")
print(f"Votos para o candidato 4: {pessoa['4']} votos ({(pessoa['4']/20)*100:.2f}%)")
print(f"Votos nulos: {pessoa['5']} votos ({(pessoa['5']/20)*100:.2f}%)")
print(f"Votos em branco: {pessoa['6']} votos ({(pessoa['6']/20)*100:.2f}%)")