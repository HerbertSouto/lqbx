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
