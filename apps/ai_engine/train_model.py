import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = Path(__file__).resolve().parent

def train_and_save_model(dataset):
    """
    dataset = [
        ("Exam will be held...", "examination"),
        ("Holiday announced...", "holiday"),
        ...
    ]
    """
    texts = [d[0] for d in dataset]
    labels = [d[1] for d in dataset]

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(X, labels)

    with open(BASE_DIR / "category_model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open(BASE_DIR / "vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Model + vectorizer saved successfully!")
