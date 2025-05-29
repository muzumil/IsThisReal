# explainer.py
import shap
import joblib

def explain(text):
    vectorizer, clf = joblib.load('model.pkl')
    explainer = shap.Explainer(clf, vectorizer.transform)
    shap_values = explainer([text])
    shap.plots.text(shap_values[0])  # Show explanation
