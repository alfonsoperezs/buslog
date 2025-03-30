import pytesseract
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
    # TODO preprocessing the image before convert to text
    custom_config = r'--oem 3 --psm 4'
    return pytesseract.image_to_string(Image.open(image_path), config=custom_config)

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
