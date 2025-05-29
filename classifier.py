# classifier.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd

def train_model():
    df = pd.read_csv('liar_dataset.csv')  # Replace with actual dataset
    X = df['statement']
    y = df['label'].apply(lambda x: 1 if str(x).strip().lower() == 'true' else 0)




    vectorizer = TfidfVectorizer(max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    clf = LogisticRegression()
    print("Label counts:\n", y.value_counts())
    clf.fit(X_vec, y)

    joblib.dump((vectorizer, clf), 'model.pkl')

def predict(text):
    vectorizer, clf = joblib.load('model.pkl')
    vec = vectorizer.transform([text])
    return clf.predict(vec)[0]
if __name__ == "__main__":
    train_model()

