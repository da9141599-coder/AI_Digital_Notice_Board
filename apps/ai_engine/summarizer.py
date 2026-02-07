from nltk.tokenize import sent_tokenize

def summarize_text(text: str, limit: int = 2):
    sentences = sent_tokenize(text)
    if len(sentences) <= limit:
        return text
    return " ".join(sentences[:limit])
