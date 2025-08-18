Claro! Aqui está o conteúdo atualizado do `README.md`, agora incluindo o script `save_data_mysql.py` como parte do projeto:

---

# 📦 Projeto: Extração e Transformação de Dados de Produtos

Este projeto realiza a extração de dados de uma API pública, armazena os dados em uma base MongoDB e realiza transformações para análise e exportação em formato CSV. Também inclui integração com MySQL para estruturação e armazenamento dos dados transformados.

## 🧩 Estrutura do Projeto

- `extract_and_save_data.py`: Script responsável por extrair dados da API e armazená-los em uma coleção MongoDB.
- `transform_data.py`: Script que realiza transformações nos dados armazenados, como renomear colunas, filtrar por datas e salvar em CSV.
- `save_data_mysql.py`: Script que prepara o ambiente MySQL, criando banco de dados e tabelas para armazenar os dados transformados.

## 🚀 Tecnologias Utilizadas

- Python
- MongoDB
- MySQL
- Pandas
- Requests

## 🔧 Pré-requisitos

- Python 3.8+
- MongoDB Atlas ou instância local
- MySQL Server ativo
- Bibliotecas Python:
  - `pymongo`
  - `pandas`
  - `requests`
  - `mysql-connector-python`

```bash
pip install pymongo pandas requests mysql-connector-python
```

## 📥 Extração e Armazenamento (`extract_and_save_data.py`)

Este script realiza:

1. Conexão com o MongoDB via URI.
2. Criação/conexão com o banco de dados `Zimo_produtos2`.
3. Criação/conexão com a coleção `produtos2`.
4. Extração de dados da API: https://labdados.com/produtos
5. Inserção dos dados na coleção MongoDB.

### ⚠️ Atenção

Substitua `"INSERT YOUR URI HERE"` pela URI da sua instância MongoDB Atlas.

## 🔄 Transformação de Dados (`transform_data.py`)

Este script realiza:

1. Conexão com o banco e coleção MongoDB.
2. Filtragem de documentos com datas de compra entre 2021 e 2029 usando regex.
3. Conversão dos dados filtrados em um DataFrame.
4. Formatação da coluna de data para o padrão `YYYY-MM-DD`.
5. Exportação dos dados para o arquivo `data/tabela2_2021_em_diante.csv`.

## 🗄️ Integração com MySQL (`save_data_mysql.py`)

Este script realiza:

1. Conexão com o servidor MySQL.
2. Criação de banco de dados.
3. Visualização de bancos existentes.
4. Criação de tabela de produtos com os campos:
   - `id`: identificador único
   - `nome_produto`: nome do produto
   - `preco`: preço do produto
5. Visualização de tabelas existentes.
6. Leitura de arquivos CSV com dados de produtos.

> ⚠️ Este script prepara o ambiente MySQL, mas não realiza a inserção dos dados no banco. Essa funcionalidade pode ser adicionada posteriormente.

## 📁 Saída

- Arquivo CSV com os dados filtrados e formatados: `data/tabela2_2021_em_diante.csv`

## 📌 Observações

- O projeto pode ser expandido com visualizações, análises estatísticas ou integração com dashboards.
- Certifique-se de que o diretório `data/` existe antes de executar o script de transformação.
- Para usar o MySQL, o servidor deve estar ativo e acessível.

## 🧑‍💻 Autor

**Symon Oliveira Mantovani**  
Cargo: Estagiário

---

Se quiser, posso gerar esse arquivo atualizado para você. Deseja que eu crie ou substitua o `README.md` com esse conteúdo?