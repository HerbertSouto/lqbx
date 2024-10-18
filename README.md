# Projeto de Análise de Dados com Python

Este projeto tem como objetivo realizar consultas em um banco de dados MySQL, manipular os dados obtidos e criar visualizações usando Python. O projeto utiliza as bibliotecas `pandas`, `mysql-connector-python`, `matplotlib` e `python-dotenv` para análise de dados e visualização e `Mkdocs` para documentação.

## Documentação Completa

Para acessar a documentação completa do projeto, visite: [Documentação do Projeto](https://herbertsouto.github.io/lqbx/)

## Estrutura do Projeto

- `database.py`: Classe responsável pela conexão com o banco de dados MySQL e pela execução de consultas SQL.
- `case_1.py`: Verifica a função de recuperação de dados da tabela `data_product_sales`.
- `case_2.py`: Script que processa e analisa dados de vendas de produtos, calculando o ticket médio por loja.
- `case_3.py`: Script que analisa os filmes da tabela IMDB, exibindo o lançamento de filmes por gênero ao longo dos anos.

## Pré-requisitos

Antes de executar o projeto, você precisa ter o seguinte instalado:

- Python 3.

- Bibliotecas Python necessárias:

  ```bash
  pip install pandas mysql-connector-python matplotlib mkdocs