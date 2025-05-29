from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict(text):
    # Limit to 512 tokens worth of characters (~2000 chars safely)
    short_text = text[:2000]  
    result = classifier(short_text)[0]
    label = "REAL" if result['label'] == "POSITIVE" else "FAKE"
    score = result['score']
    return label, score
