import matplotlib.pyplot as plt
import pandas as pd
from database import Database
import os
from dotenv import load_dotenv

load_dotenv()

class MovieVisualizer:
    def __init__(self, db):
        self.db = db

    def fetch_movies_data(self):
        query = "SELECT Genre, Votes, Year FROM IMDB_movies"
        movies_df = self.db.execute_query(query)
        return movies_df

    def plot_genre_distribution_by_year(self):
        movies_df = self.fetch_movies_data()

        # Quebrar os gêneros em linhas separadas
        movies_df['Genre'] = movies_df['Genre'].str.split(',')
        movies_exploded = movies_df.explode('Genre')

        # Contar a quantidade de filmes por gênero e ano
        genre_year_counts = movies_exploded.groupby(['Year', 'Genre']).size().unstack(fill_value=0)

        # Criar um gráfico de barras empilhadas
        genre_year_counts.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='tab20')

        # Adicionar títulos e rótulos
        plt.title('Distribuição de Filmes por Gênero ao Longo dos Anos', fontsize=16)
        plt.xlabel('Ano', fontsize=14)
        plt.ylabel('Número de Filmes', fontsize=14)
        plt.xticks(rotation=45)

        plt.tight_layout()  # Ajusta o layout para evitar sobreposição
        plt.show()

if __name__ == "__main__":
    # Conexão ao banco de dados e execução do visualizador
    db = Database(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    visualizer = MovieVisualizer(db)
    visualizer.plot_genre_distribution_by_year()

    db.close()

