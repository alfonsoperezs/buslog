import pytesseract
from PIL import Image
from exceptions import ParsingError

def extract_text(image: str) -> str:
    return pytesseract.image_to_string(Image.open(image))

def process_text(text: str) -> list:
    return text.split('\n')

def obtain_data(data: list) -> dict:
    try:
        line = next((s.split("+")[-1].strip() for s in data if s.startswith("Linea") and "+" in s))
        date = next((s.split(": ")[-1] for s in data if s.startswith("Fecha") and ": " in s))
        stop = next((s.split(": ")[-1] for s in data if s.startswith("Origen") and ": " in s))
    except StopIteration:
        raise ParsingError("Can't find all necesary data")
    
    return {"Line": line, "Date": date, "Stop": stop}


if __name__ == '__main__':
    l = process_text(extract_text('test.jpg'))
    d = obtain_data(l)
    print(d)