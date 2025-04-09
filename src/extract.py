import pytesseract
import cv2
import numpy as np
from PIL import Image
from exceptions import ParsingError

def extract_text(image_path: str) -> str:
    """Convert a image to text

    Params:
        image_path (str): Path to the image file.

    Return:
        str: Extracted text from the image.

    Raises:
        FileNotFoundError: If the image file does not exist.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {path}")
    kernel = np.ones((2, 2), np.uint8)
    kernel2 = np.ones((3, 3), np.uint8)
    img = cv2.morphologyEx(img , cv2.MORPH_CLOSE, kernel)
    img = cv2.morphologyEx(img , cv2.MORPH_OPEN, kernel2)
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    custom_config = r'--oem 3 --psm 4'
    return pytesseract.image_to_string(img_pil, config=custom_config)

def process_text(text: str) -> list:
    """Processes a text by splitting it into lines.

    Args:
        text (str): The input text.

    Returns:
        list: A list of strings, each representing a line from the text.
    """
    return text.split('\n')

def obtain_data(data: list) -> dict:
    """Extracts specific data from a list of text lines.

    Args:
        data (list): A list of strings containing various information.

    Returns:
        dict: A dictionary with extracted values:
            - "Line" (str): The bus line information.
            - "Date" (str): The date of the transaction.
            - "Stop" (str): The origin stop.

    Raises:
        ParsingError: If any required data is missing.
    """
    try:
        line = next((s.split(": ")[-1].strip() for s in data if s.startswith("Linea") and ":" in s))
        date = next((s.split(": ")[-1] for s in data if s.startswith("Fecha") and ": " in s))
        stop = next((s.split(": ")[-1] for s in data if s.startswith("Origen") and ": " in s))
    except StopIteration:
        raise ParsingError("Can't find all necesary data")
    
    return {"Line": line, "Date": date, "Stop": stop}
