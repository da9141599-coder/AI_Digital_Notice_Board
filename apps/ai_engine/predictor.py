import os
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "category_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

# Keyword fallback (if model missing)
KEYWORD_MAP = {
    "exam": "examination",
    "schedule": "timetable",
    "holiday": "holiday",
    "fee": "finance",
    "payment": "finance",
    "meeting": "event",
    "sports": "sports",
    "placement": "placement",
    "campus": "campus",
}


def _fallback_category(text: str):
    text = text.lower()
    for word, cat in KEYWORD_MAP.items():
        if word in text:
            return cat
    return "general"


def predict_category(text: str) -> str:
    """
    Predicts category using ML model if available.
    Falls back to keyword-based classification.
    """
    if MODEL_PATH.exists() and VECTORIZER_PATH.exists():
        try:
            with open(MODEL_PATH, "rb") as f:
                model = pickle.load(f)
            with open(VECTORIZER_PATH, "rb") as vf:
                vectorizer = pickle.load(vf)

            vec = vectorizer.transform([text])
            prediction = model.predict(vec)[0]
            return prediction
        except Exception:
            return _fallback_category(text)

    return _fallback_category(text)
