import pandas as pd
from database import Database
import os
from dotenv import load_dotenv


load_dotenv()


class QueryProcessor:
    def __init__(self, db: Database):
        self.db = db

    def fetch_stores(self):
        query = """
        SELECT
            STORE_CODE,
            STORE_NAME,
            BUSINESS_NAME,
            BUSINESS_CODE
        FROM data_store_cad
        """
        return self.db.execute_query(query)

    def fetch_sales(self, start_date, end_date):
        query = f"""
        SELECT
            STORE_CODE,
            DATE,
            SALES_VALUE,
            SALES_QTY
        FROM data_store_sales
        WHERE DATE BETWEEN '{start_date}' AND '{end_date}'
        """
        return self.db.execute_query(query)

    def process_queries(self, start_date, end_date):
        stores_df = self.fetch_stores()
        sales_df = self.fetch_sales(start_date, end_date)

        merged_df = pd.merge(stores_df, sales_df, on='STORE_CODE', how='left')

        average_sales_df = merged_df.groupby(['STORE_NAME', 'BUSINESS_NAME']).agg(
            Average_Sales_Value=('SALES_VALUE', 'sum'),
            Total_Sales_Qty=('SALES_QTY', 'sum')
        ).reset_index()

        # Calcula a média e arredonda
        average_sales_df['TM'] = average_sales_df.apply(
            lambda row: round(row['Average_Sales_Value'] / row['Total_Sales_Qty'], 2) if row['Total_Sales_Qty'] > 0 else 0, 
            axis=1
        )

        # Renomeia as colunas conforme o necessário
        average_sales_df = average_sales_df[['STORE_NAME', 'BUSINESS_NAME', 'TM']]
        average_sales_df.columns = ['Loja', 'Categoria', 'TM']

        return average_sales_df

if __name__ == "__main__":
    # Crie uma instância da classe Database com as credenciais
    db = Database(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    
    # Crie um processador de consultas e processa as consultas
    processor = QueryProcessor(db)
    result_df = processor.process_queries('2019-10-01', '2019-12-31')
    
    # Exibe o resultado no formato desejado
    print(result_df.to_string(index=False))

    # Fecha a conexão
    db.close()


