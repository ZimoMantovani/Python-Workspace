import mysql.connector  
import pandas as pd

def connect_mysql(host_name, user_name, pw):

    cnx =  mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=pw
    )
    return cnx

def create_cursor(cnx):
    cursor = cnx.cursor()
    return cursor
    
def create_database(cursor, db_name): 
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")

def show_databases(cursor):
    cursor.execute("SHOW DATABASES;")
    for db in cursor:
        print(db)
        
def create_product_table(cursor, db_name, tb_name):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {db_name}.{tb_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_produto VARCHAR(255),
            preco DECIMAL(10,2)
        );
    """)

def show_tables(cursor, db_name):
    cursor.execute(f"USE {db_name};")
    cursor.execute("SHOW TABLES;")
    for db in cursor:
        print(db)
    
def read_csv(path):
    pd.read_csv(path)

# cnx = connect_mysql("HOST","USER","PASSWORD")
# cursor = create_cursor(cnx)
# create_database(cursor, 'DATABASENAME')
# show_databases(cursor)
# create_product_table(cursor,"DATABASENAME","TABLE_NAME")
# show_tables(cursor, "DATABASENAME")
