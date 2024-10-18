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
                
            query = "SELECT * FROM data_product_sales WHERE 1=1"  # Começar a consulta com um true
            params = []

            if product_code is not None:
                query += " AND product_code = %s"
                params.append(product_code)

            if store_code is not None:
                query += " AND store_code = %s"
                params.append(store_code)

            if date is not None and len(date) == 2:
                query += " AND date BETWEEN %s AND %s"
                params.extend(date)

            # Executa a consulta
            with self.cnx.cursor() as cur:
                cur.execute(query, params)
                results = cur.fetchall()
            
            # Cria um DataFrame com os resultados
            df = pd.DataFrame(results, columns=[i[0] for i in cur.description])
            return df

        except Error as e:
            print(f"Error: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
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
