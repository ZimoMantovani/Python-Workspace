
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "INSERT YOUR URI HERE"

# Estabelece a conexão com a instância do MongoDB usando a URI fornecida. 
# Ela retorna o cliente do MongoDB que permite interagir com o banco de dados.
def connect_mongo(uri):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)        
    return client

# Utiliza o(a) cliente do MongoDB para criar (se não existir) e conectar-se ao banco de dados especificado pelo parâmetro db_name. 
# Ela retorna o objeto de banco de dados que pode ser usado para interagir com as coleções dentro dele.
def create_connect_db(client, db_name):
    db = client[db_name] 
    return db

#cria (se não existir) e conecta-se à coleção especificada pelo parâmetro col_name dentro do banco de dados fornecido. 
# Ela retorna o objeto de coleção que pode ser usado para interagir com os documentos dentro dela.
def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection

#Extrai dados de uma API na URL fornecida e retorna os dados extraídos no formato JSON.
def extract_api_data(url):
    response = requests.get(url)
    return response.json()

#Recebe uma coleção e os dados que serão inseridos nela. Ela deve adicionar todos os documentos à coleção e retornar a quantidade de documentos inseridos.  
def insert_data(col, data):
  
    docs = col.insert_many(data)

    return len(docs.inserted_ids)


def close_mongo(client):
    client.close()

client = connect_mongo(uri)
db = create_connect_db(client,"Zimo_produtos2")
collection = create_connect_collection(db,"produtos2")
responseJson = extract_api_data("https://labdados.com/produtos")
size = insert_data(collection,responseJson)

close_mongo(client)