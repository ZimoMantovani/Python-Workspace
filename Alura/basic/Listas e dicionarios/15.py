# 15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. 
# Para isso, foram fornecidos os seguintes dados:

'''
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
'''
#Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, 
# a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
            'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
            'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
            'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
            }

valoresIdades = list(idades.values())
setores = list(idades.keys())
media = []
todasIdades = []
qtdTotalFuncionario = []
acima_da_media = 0

for i in range(len(valoresIdades)):
    media_atual = sum(valoresIdades[i]) / len(valoresIdades[i])
    media.append(media_atual)
    print(f'Media do {setores[i]}: {media_atual}')
    
    #Soma a idade de cada setor 
    coletorIdade = sum(valoresIdades[i])
    todasIdades.append(coletorIdade)
    
    #Soma a quantidade de funcionarios em cada setor
    coletorFuncionario = len(valoresIdades[i])
    qtdTotalFuncionario.append(coletorFuncionario)
    
#Divide a soma do total da idade de todos os funcionarios pela quantidade total de funcionarios na empresa
media_todos = sum(todasIdades) / sum(qtdTotalFuncionario)


for lista in valoresIdades:
    for idade in lista:
        print(idade)
        if idade > media_todos:
            acima_da_media += 1
print(f'Quantidade de pessoas acima da média geral ({media_todos:.2f} anos): {acima_da_media}')