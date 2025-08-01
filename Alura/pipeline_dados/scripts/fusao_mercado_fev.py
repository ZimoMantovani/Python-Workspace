import json
import csv


#Retorna as colunas
def get_columns(dados):
    return list(dados[-1].keys())

#Retorna a lista de produtos da empresa A
def leitura_json(path_json):

    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json


#Retorna a lista de produtos da empresa B
def leitura_csv(path_csv):
    
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv


#Junta as duas funções Json e CSV e retorna em 'dados'
def leitura_dados(path, tipo_arquivo):
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
        
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados


#Renomeia as colunas com os novos nomes do key_mapping
def rename_columns(dados, key_mapping):
    
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

#Retorna a quantidade de produtos em uma lista
def size_data(dados):
    return len(dados)

#Combina os dados
def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

#Caminho para a base de dados
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


#Faz a leitura dos dados 

#JSON
dados_json =  leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f'Nome das colunas em Json {nome_colunas_json}')
print(f'Tamanho dos dados Json {tamanho_dados_json}')

#CSV
dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f'Nome das colunas em CSV {nome_colunas_csv}')
print(f'Tamanho dos dados CSV {tamanho_dados_csv}')


#Transformações dos dados

#Mapa dos novos nomes das colunas
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
key_mapping


#Transformação dos dados CSV

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f'Nome das colunas CSV (RENOMEADAS){nome_colunas_csv}')

dados_fusao = join(dados_json,dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(f'Tabelas fundidas: {nome_colunas_fusao}')
print(f'Tamanho dos dados fundidos {tamanho_dados_fusao}')
