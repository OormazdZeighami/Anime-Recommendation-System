
<!-- Banner -->
<p align="center">
  <img src="https://raw.githubusercontent.com/oormazdam/assets/main/Anime-Recommendation-System-Banner.svg" alt="Anime Recommendation System Banner" />
</p>

<h1 align="center">🎌 Anime Recommendation System</h1>
<h3 align="center">A simple content-based recommendation engine built with Python and pandas</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/Powered_by-Scikit--Learn-yellow" />
</p>

---

## 🧠 About the Project

This is a **content-based anime recommender system** that uses anime genres to find and suggest similar shows.

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020) and includes titles, genres, scores, and other metadata.

### 🔍 How It Works

- Loads and preprocesses the anime dataset
- Uses TF-IDF vectorization on genres
- Calculates cosine similarity between anime
- Takes user input and recommends 5 similar anime

---

## 🚀 Demo

```bash
$ python recommendation.py
🎉 Welcome to the Anime Recommendation System!

Enter an anime name (or 'exit' to quit): death note

🎬 Code Geass: Hangyaku no Lelouch (Score: 8.89)
🎬 Monster (Score: 8.76)
🎬 Zankyou no Terror (Score: 7.85)
🎬 Ergo Proxy (Score: 7.92)
🎬 Psycho-Pass (Score: 8.42)
```

---

## 🛠 Technologies Used

- Python 3
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📁 Project Structure

```
Anime-Recommendation-System/
│
├── data/
│   └── anime.csv               # Dataset file (not included in repo)
│
├── recommendation.py           # Main Python script
├── requirements.txt            # Required Python packages
├── LICENSE                     # MIT License
└── README.md                   # This file
```

> ⚠️ **Note:** The `anime.csv` dataset is not included in this repository due to size and licensing. You can download it from Kaggle and place it inside the `data/` folder.

---

## 📝 How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/OormazdZeighami/Anime-Recommendation-System.git
   cd Anime-Recommendation-System
   ```

2. **Install the dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**  
   Download from [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020)  
   Place the `anime.csv` file inside the `data/` folder.

4. **Run the recommender**  
   ```bash
   python recommendation.py
   ```

---

## 📫 Contact

Made with ❤️ by **[Oormazd Zeighami](https://github.com/OormazdZeighami)**  
📧 Email: oormazdighami@gmail.com  
💼 Portfolio coming soon!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software with attribution.

---

## 🔎 GitHub SEO Tips

- Use clear and relevant repository name (`Anime-Recommendation-System`)
- Add proper **topics/tags**:  
  *(e.g.,)* `anime`, `recommendation-system`, `python`, `content-based-filtering`, `machine-learning`, `data-science`
- Add a good project **description** in your repo settings:  
  `A content-based anime recommender system using genre similarity (TF-IDF + cosine similarity)`
- Add a **social preview image** to the repo (if you want, I can design one with your banner)
- Link the repo in your personal website or portfolio (for backlinking)
