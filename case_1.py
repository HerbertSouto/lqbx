import os
from dotenv import load_dotenv
from database import Database

load_dotenv()

def test_retrieve_data():
    db = Database(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    # Teste
    my_data = db.retrieve_data(
        product_code=[18, 48, 172],
        store_code=[1, 2, 3],
        date=['2019-01-01', '2019-01-31']
    )
    
    # Imprime os dados retornados
    print("Dados retornados:")
    print(my_data)
    
    db.close()

if __name__ == "__main__":
    test_retrieve_data()