import requests
import pandas as pd
import json
import math

# Extração
class dadosRepositorios:
    def __init__(self,owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = 'meutoken'  
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    #Paginação
    #Pega todas as paginas dos repositorios publicos
    def verifca_pags(self):
            url = f'{self.api_base_url}/users/{self.owner}'
            response = requests.get(url, headers=self.headers)
            total_repos = response.json()['public_repos']
            total_pags = total_repos/30
            math.ceil(total_pags)
            return total_pags
        
    #Cria uma lista com todos os repositorios
    def lista_repositorios(self):
        repos_list = []
        total_pags = int(self.verifca_pags())
        for page_num in range(1,total_pags+2):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list
    
    #Coleta o nome dos repositorios
    def nome_repos(self,repos_list):
        repos_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass
        return repos_names
    
    #Coleta as linguagens dos repositorios
    def nome_linguagens(self,repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
        return repo_languages
    
    #Criação do dataframe 
    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.nome_repos(repositorios)
        linguagens = self.nome_linguagens(repositorios)
        
        dados = pd.DataFrame()
        dados['repositoriy_name'] = nomes
        dados['language'] = linguagens
        
        return dados


amazon_rep = dadosRepositorios("amzn")
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()
#print(ling_mais_usadas_amzn)

netflix_rep = dadosRepositorios("netflix")
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()
#print(ling_mais_usadas_netflix)

spotify_rep = dadosRepositorios("spotify")
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()
#print(ling_mais_usadas_spotify)

apple_rep = dadosRepositorios("APPLE")
ling_mais_usadas_apple = apple_rep.cria_df_linguagens()
#print(ling_mais_usadas_apple)

#Salvandos os dados
ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')