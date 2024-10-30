import mysql.connector
import pandas as pd
from mysql.connector import Error

class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection ok.")
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.cnx.is_connected():
            self.cnx.close()
            print("Connection closed.")

    def retrieve_data(self, product_code=None, store_code=None, date=None):
        """Recupera dados da tabela data_product_sales com base nos parâmetros fornecidos."""
        try:
            if self.cnx is None or not self.cnx.is_connected():
                self.connect()
                
            # Consulta inicial que sempre é verdadeira para facilitar a adição de filtros
            query = "SELECT * FROM data_product_sales WHERE 1=1"
            params = []

            # Verifica se product_code é uma lista de códigos ou um único código
            if product_code is not None:
                if isinstance(product_code, (list, tuple)):
                    # Se for uma lista/tupla, usa a cláusula IN
                    placeholders = ', '.join(['%s'] * len(product_code))
                    query += f" AND product_code IN ({placeholders})"
                    params.extend(product_code)
                else:
                    # Caso contrário, usa igualdade simples
                    query += " AND product_code = %s"
                    params.append(product_code)

            if store_code is not None:
                if isinstance(store_code, (list, tuple)):
                    placeholders = ', '.join(['%s'] * len(store_code))
                    query += f" AND store_code IN ({placeholders})"
                    params.extend(store_code)
                else:
                    query += " AND store_code = %s"
                    params.append(store_code)

            if date is not None:
                if isinstance(date, (list, tuple)) and len(date) == 2:
                    query += " AND date BETWEEN %s AND %s"
                    params.extend(date)
                else:
                    print("Formato de data inválido. Use uma lista ou tupla com duas datas [início, fim].")
                    return pd.DataFrame()

            # Executa a consulta
            with self.cnx.cursor() as cur:
                cur.execute(query, params)
                results = cur.fetchall()
            
            # Cria um DataFrame com os resultados
            df = pd.DataFrame(results, columns=[i[0] for i in cur.description])
            return df

        except Error as e:
            print(f"Error: {e}")
            return pd.DataFrame()

    def execute_query(self, query):
        """Executa uma consulta SQL e retorna um DataFrame."""
        if self.cnx is None or not self.cnx.is_connected():
            self.connect()
        try:
            df = pd.read_sql(query, self.cnx)
            return df
        except Error as e:
            print(f"Error executing query: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
