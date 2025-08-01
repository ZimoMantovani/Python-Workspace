import json
import csv

from processamentos_dados import Dados

#Combina os dados
def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

#Transformando dados
def transformando_dados_tabela(dados,nome_colunas):
    dados_combinados_tabela = [nome_colunas]
    for row in dados:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna,'Indisponivel'))
        dados_combinados_tabela.append(linha)
        
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path,'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

#Caminho para a base de dados
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# extract
dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print(dados_empresaA.nome_colunas)
#print(dados_empresaB.nome_colunas)
print(dados_empresaA.qtd_linhas)


# transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
key_mapping

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# #Faz a leitura dos dados 

# #JSON
# dados_json =  leitura_dados(path_json, 'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)
# print(f'Nome das colunas em Json {nome_colunas_json}')
# print(f'Tamanho dos dados Json {tamanho_dados_json}')

# #CSV
# dados_csv = leitura_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)
# print(f'Nome das colunas em CSV {nome_colunas_csv}')
# print(f'Tamanho dos dados CSV {tamanho_dados_csv}')


# #Transformações dos dados

# #Mapa dos novos nomes das colunas
# key_mapping = {'Nome do Item': 'Nome do Produto',
#                 'Classificação do Produto': 'Categoria do Produto',
#                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
#                 'Quantidade em Estoque': 'Quantidade em Estoque',
#                 'Nome da Loja': 'Filial',
#                 'Data da Venda': 'Data da Venda'}
# key_mapping


# #Transformação dos dados CSV

# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(f'Nome das colunas CSV (RENOMEADAS){nome_colunas_csv}')

# dados_fusao = join(dados_json,dados_csv)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(f'Tabelas fundidas: {nome_colunas_fusao}')
# print(f'Tamanho dos dados fundidos {tamanho_dados_fusao}')

# #Salvando os dados
# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = 'data_processed/dados_combinados.csv'

# salvando_dados(dados_fusao_tabela,path_dados_combinados)
# print(path_dados_combinados)