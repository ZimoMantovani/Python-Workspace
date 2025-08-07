# ManipulaRepositorios - Automatizando Criação e Upload de Repositórios no GitHub

Este projeto contém um script Python que automatiza a criação de repositórios no GitHub e o upload de arquivos para esses repositórios. Ele utiliza a API do GitHub para facilitar o gerenciamento de dados de forma programática.

## Funcionalidades

- Criação de repositórios públicos no GitHub.
- Upload de arquivos locais para o repositório criado.
- Codificação dos arquivos em base64 para compatibilidade com a API do GitHub.

## Estrutura

O script define uma classe chamada `ManipulaRepositorios`, que recebe o nome de usuário do GitHub e utiliza um token de acesso para autenticação.

### Métodos principais:

- `cria_repo(nome_repo)`: Cria um novo repositório com nome e descrição definidos.
- `add_arquivo(nome_repo, nome_arquivo, caminho_arquivo)`: Adiciona arquivos ao repositório especificado.

## Requisitos

- Python 3.x
- Biblioteca `requests`

## Observações

- O token de acesso deve ser gerado no GitHub com permissões adequadas e substituído no campo `self.access_token`.
- Os arquivos adicionados estão disponíveis no repositório criado: [linguagens-repositorios-empresas](https://github.com/ZimoMantantovani**  
Estagiário e entusiasta de automações com Python.
