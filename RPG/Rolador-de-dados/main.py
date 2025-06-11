import random
import mysql.connector

from tkinter import *
from tkinter import ttk

#Configuração do banco de dados
mydb = mysql.connector.connect(host="localhost", user="root",passwd="", database="bd_armazenar_dados")
cursor = mydb.cursor()


def rolar_dado(comando):
    try:
        # Separar a parte do modificador
        if '+' in comando:
            dado_part, sepSoma = comando.split('+')
            sepSoma = int(sepSoma)
        else:
            dado_part = comando
            sepSoma = 0

        # Separar quantidade e tipo de dado
        qtd_dados, tipo_dado = dado_part.split('d')
        qtd_dados = int(qtd_dados) if qtd_dados else 1  # Se não houver número antes do d, assume 1
        tipo_dado = int(tipo_dado)

        # Rolar os dados
        valor = [random.randint(1, tipo_dado) for _ in range(qtd_dados)]
        total = sum(valor) + sepSoma

        # adiciona o valor dos resultados a uma variavel para utilizar no Tkinter
        resultados = f'''
        
        Resultados individuais: {valor}
        Total com modificador: {total}'''
        
        texto_resultados["text"] = resultados
        
        #Insere os resultados totais no BD
        insere_sql = "INSERT INTO dados (resultados) VALUES (%s)"
        cursor.execute(insere_sql, (total,))
        mydb.commit()
        print(cursor.rowcount, "Registrado na tabela")
        
        
        
    except (ValueError, AttributeError):
        texto_resultados["text"] = "Formato inválido. Use algo como '2d6+1' ou 'd20'."

root = Tk()


#Criação do grid
root.geometry("250x250")
root.title("Rolagem de dados")
root.config(bg="lightblue")

# Configuração para centralização automática
root.grid_rowconfigure(0, weight=1)  # Faz a linha 0 expandir
root.grid_columnconfigure(0, weight=1)  # Faz a coluna 0 expandir

#Label incial
texto_orientacao = Label(root, text = "Digite o dado para rolar (ex: 2d6+1): ")
texto_orientacao.grid(column=0,row=0,padx=3,pady=3)

#Valor do dado inserido
valor_text = Entry(root, width=30)
valor_text.grid(column=0, row=1, padx=5, pady=5)

#Botão chama a função de rolagem de dados
botao = Button(root, text="Rolar dados!", command=lambda:rolar_dado(valor_text.get()))
botao.grid(column=0,row=2,padx=5,pady=5)

#Mostra o resultado
texto_resultados = Label(root, text="")
texto_resultados.grid(column=0,row=3,padx=5,pady=5, sticky="nsew")

root.mainloop()
cursor.close()