# Projeto de Análise de Dados com Python

Este projeto tem como objetivo realizar consultas em um banco de dados MySQL, manipular os dados obtidos e criar visualizações usando Python. O projeto utiliza as bibliotecas `pandas`, `mysql-connector-python`, `matplotlib` e `python-dotenv` para análise de dados e visualização e `Mkdocs` para documentação.

## Documentação Completa

Para acessar a documentação completa do projeto, visite: [Documentação lqbx](https://herbertsouto.github.io/lqbx/)

## Estrutura do Projeto

- `database.py`: Classe responsável pela conexão com o banco de dados MySQL e pela execução de consultas SQL.
- `case_1.py`: Verifica a função de recuperação de dados da tabela `data_product_sales`.
- `case_2.py`: Script que processa e analisa dados de vendas de produtos, calculando o ticket médio por loja.
- `case_3.py`: Script que analisa os filmes da tabela IMDB, exibindo o lançamento de filmes por gênero ao longo dos anos.

# Como usar

## Configuração do ambiente
Clone o repositório:

```bash
git clone https://github.com/HerbertSouto/lqbx.git
```
Instale as dependências usando `poetry install` ou `pip install -r requirements.txt`.

```bash
poetry install
```

3. Configure as variáveis de ambiente para conexão ao banco de dados, altere o arquivo ".env-example" com suas credenciais e renomeie para ".env":

```bash
DB_HOST=seu_host
DB_PORT=3306
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

## Executando o projeto

Para executar o script:

```bash
poetry run python case_1.py
```
```bash
poetry run python case_2.py
```
```bash
poetry run python case_3.py
```
