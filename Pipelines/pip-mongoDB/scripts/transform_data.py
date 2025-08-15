from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection, close_mongo
import pandas as pd

uri = "INSERT YOUR URI HERE"

client = connect_mongo(uri)
db = create_connect_db(client, "Zimo_produtos2")
collection = create_connect_collection(db, "produtos2")

def visualize_collection(col):
    for doc in col.find():
        print(doc)

def rename_column(col, col_name, new_name):
    print(col.update_many({}, {"$rename": {col_name: new_name}}))

def select_category(col, category):
    print(col.distinct(category))

def make_regex(col, regex):
    query = {"Data da Compra": {"$regex": f"{regex}"}}

    lista_regex = []
    for doc in col.find(query):
        lista_regex.append(doc)
    
    return lista_regex

def create_dataframe(lista):
    df =  pd.DataFrame(lista)
    return df

def format_date(df):
    df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")
    df['Data da Compra'] = df['Data da Compra'].dt.strftime('%Y-%m-%d')
   
def save_csv(df, path):
    
   df.to_csv(path)
   
   
#def create_dataframe(lista): 
    
    
#visualize_collection(collection)

#rename_column(collection,"lat","Latitude")

#select_category(collection, "Categoria do Produto")

lista_regex = make_regex(collection, "/202[1-9]")

df_produtos= create_dataframe(lista_regex)

format_date(df_produtos)

save_csv(df_produtos,"data/tabela2_2021_em_diante.csv")

close_mongo(client)