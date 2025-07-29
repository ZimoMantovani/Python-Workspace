# 12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças.
# A pesquisa foi feita e o votos computados podem ser observados abaixo:

'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''

# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

votos = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210,
    "Design 5": 1811
}

totalVotos = sum(votos.values())
maisVotado = max(votos.values())


    
for design, votos_design in votos.items():
    porcentagem = (votos_design * 100) / totalVotos
    print(f'{design} com {porcentagem:.2f}% dos votos')
    
    
    
vencedor = max(votos, key=votos.get)
print(f'Vencedor: {vencedor} com {votos[vencedor]} votos')