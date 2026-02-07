import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an uploaded notice image.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception:
        return ""
