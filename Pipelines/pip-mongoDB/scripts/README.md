# 📦 Projeto: Extração e Transformação de Dados de Produtos

Este projeto realiza a extração de dados de uma API pública, armazena os dados em uma base MongoDB e realiza transformações para análise e exportação em formato CSV.

## 🧩 Estrutura do Projeto

- `extract_and_save_data.py`: Script responsável por extrair dados da API e armazená-los em uma coleção MongoDB.
- `transform_data.py`: Script que realiza transformações nos dados armazenados, como renomear colunas, filtrar por datas e salvar em CSV.

## 🚀 Tecnologias Utilizadas

- Python
- MongoDB
- Pandas
- Requests

## 🔧 Pré-requisitos

- Python 3.8+
- MongoDB Atlas ou instância local
- Biblioteca `pymongo` instalada
- Biblioteca `pandas` instalada

```bash
pip install pymongo pandas requests
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

## 📁 Saída

- Arquivo CSV com os dados filtrados e formatados: `data/tabela2_2021_em_diante.csv`

## 📌 Observações

- O projeto pode ser expandido com visualizações, análises estatísticas ou integração com dashboards.
- Certifique-se de que o diretório `data/` existe antes de executar o script de transformação.

## 🧑‍💻 Autor

**Symon Oliveira Mantovani**  
Cargo: Estagiário

---

Se quiser, posso gerar esse arquivo `README.md` para você automaticamente. Deseja que eu crie o arquivo?