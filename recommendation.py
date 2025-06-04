"""
Anime Recommendation System
Author: Oormazd Zeighami
Description:
    A simple content-based recommendation engine using genres similarity.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_and_clean_data(filepath):
    """
    Load and clean the dataset.
    - Fills missing genre fields.
    - Standardizes text data.
    """
    df = pd.read_csv(filepath)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    if 'genres' not in df.columns:
        print("Error: 'genres' column not found in dataset.")
        print("Available columns:", df.columns.tolist())
        exit()

    df['genres'] = df['genres'].fillna('')
    df['name'] = df['name'].fillna('Unknown')

    return df


def build_similarity_matrix(df):
    """
    Create a TF-IDF matrix from genres and calculate cosine similarity.
    """
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genres'])

    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity


def get_recommendations(title, df, similarity_matrix):
    """
    Given an anime title, return top 5 similar anime based on genres.
    """
    title = title.lower()
    indices = pd.Series(df.index, index=df['name'].str.lower())

    if title not in indices:
        return f"❌ Anime titled '{title}' not found in dataset."

    idx = indices[title]
    sim_scores = list(enumerate(similarity_matrix[idx]))

    # Sort by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i, score in sim_scores:
        recommendations.append(f"🎬 {df.iloc[i]['name']} (Score: {df.iloc[i]['score']})")

    return "\n".join(recommendations)


def main():
    print("🎉 Welcome to the Anime Recommendation System!")
    file_path = "data/anime.csv"

    df = load_and_clean_data(file_path)
    similarity = build_similarity_matrix(df)

    while True:
        anime_name = input("\nEnter an anime name (or 'exit' to quit): ")
        if anime_name.lower() == 'exit':
            print("👋 Goodbye!")
            break

        result = get_recommendations(anime_name, df, similarity)
        print(result)


if __name__ == "__main__":
    main()
