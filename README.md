# 📰 IsThisReal - Fake News Detection Tool

IsThisReal is a machine learning-based web application designed to detect and classify news content as **real** or **fake**. Built to combat misinformation, the tool uses NLP techniques and supervised learning to analyze textual data and predict its credibility.

---

## 🚀 Features
- Classifies news articles as **REAL** or **FAKE**
- Trained on a labeled dataset of verified and falsified news
- Implements preprocessing techniques like tokenization, stopword removal, and TF-IDF
- Uses logistic regression / decision trees / (custom model here)
- Clean, user-friendly interface for submitting news snippets

---

## 🛠️ Tech Stack

| Component        | Tools Used                              |
|------------------|------------------------------------------|
| Programming      | Python                                   |
| NLP Libraries    | NLTK, Scikit-learn, Pandas, NumPy        |
| Model            | Logistic Regression / Naive Bayes / etc |
| Interface        | Streamlit / Flask (choose one)           |
| Dataset          | [Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

---




## 📦 Installation

```bash
git clone https://github.com/yourusername/isthisreal.git
cd isthisreal
pip install -r requirements.txt
python app.py
