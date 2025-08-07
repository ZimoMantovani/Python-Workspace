import requests

username = 'amzn'
url = f"https://api.github.com/users/{username}/followers"

# definindo o token e a versão da API
access_token = 'meutoken'
headers = {'Authorization': 'Bearer ' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

# page = 1
# followers_list = []
# followers_name = []
# while True: 

#     # faz a requisição 
#     url_page = f'{url}?page={page}'
#     response = requests.get(url_page, headers=headers)

#     # converte a resposta para um objeto JSON
#     followers = response.json()

#     # caso a lista esteja vazia, podemos sair do laço pois todos os dados foram extraidos
#     if len(followers)==0:
#         break

#     # adicionando os seguidores a lista
#     followers_list.append(followers)

#     # incrementa o valor de 'page' para a próxima requisição
#     page += 1

# print(followers_list)
# for page in followers_list:
#     for follower in page:
#         followers_name.append(follower['name'])



# print(followers_name[:10])


# todos = 0
# for repos in followers_list:
#     todos += len(repos)
# print(todos)

api_base_url = 'https://api.github.com'
username = 'ZimoMantovani'
repo = 'app-platform'
owner = 'amzn'

url = f'{api_base_url}/repos/{owner}/{repo}/forks'
print(url)


response = requests.post(url, headers=headers)
print(response.status_code)
