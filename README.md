# BusLog

Buslog monitors delays on Galician public transport buses by analyzing the tickets issued during the journey.

## How to install

We are using [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) to extract the text from the ticket image. First of all, you need to install `tesseract`.

```
sudo apt install tesseract-ocr
```

Then, you need to install the requirements for run it.

```
pip install -r requirements.txt
```
