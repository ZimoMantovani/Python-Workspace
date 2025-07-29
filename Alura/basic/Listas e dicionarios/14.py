# 14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. 
# A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa
# floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas 
# listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
'''
{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
'''
#Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. 
# Dica: use as funções built-in sum() e len().

faunaFlora = {'Área Norte': [2819, 7236],
            'Área Leste': [1440, 9492],
            'Área Sul': [5969, 7496],
            'Área Oeste': [14446, 49688],
            'Área Centro': [22558, 45148]
            }

#fauna = {area: valores[0] for area, valores in faunaFlora.items()}
#flora = {area: valores[1] for area, valores in faunaFlora.items()}

valoresFaunaFlora = list(faunaFlora.values())
areas = list(faunaFlora.keys())
media = []

for i in range(0,5):
    media_atual = sum(valoresFaunaFlora[i]) / len(valoresFaunaFlora[i])
    media.append(media_atual)
    print(f'Media da {areas[i]}: {media_atual}')
    
indice_maior = media.index(max(media))
print(f'A maior diversidade foi de {max(media)} na {areas[indice_maior]}')

    




