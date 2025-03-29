import pytesseract
from PIL import Image

def extract_text(image: str) -> str:
    return pytesseract.image_to_string(Image.open(image))

def process_text(text: str) -> list:
    l = text.split('\n')
    while True:
        try:
            l.remove('')
        except ValueError:
            break
    return l

def obtain_data(data: list) -> dict:
    line = next((s.split("+")[-1].strip() for s in data if s.startswith("Linea")), None)
    date = next((s.split(": ")[-1] for s in data if s.startswith("Fecha")), None)
    stop = next((s.split(": ")[-1] for s in data if s.startswith("Origen")), None)
    return {"Line": line, "Date": date, "Stop": stop}


if __name__ == '__main__':
    l = process_text(extract_text('test.jpg'))
    d = obtain_data(l)
    print(d)