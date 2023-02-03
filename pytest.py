import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import pandas as pd
import re
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def ImagePreProcess(im):
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    return im

im = Image.open("1.png")
im = ImagePreProcess(im)

def linebreak(txt: str) -> str:
    """
    This function detect systematic errors and rectifies them.
    """
    pattern = [['—\s', ' '], ['‘‘\s','"'], ['\s‘‘','"'], ['-\s', ' ']]
    for i in pattern:
        txt = re.sub(i[0], i[1], txt)
    return txt

def ImageToText(im):
    data = pytesseract.image_to_data(im, output_type='data.frame')
    df = pd.DataFrame(data)
    df.dropna(subset=['text'], inplace=True)
    df.reset_index(inplace=True)
    df['text'].apply(linebreak)
    df['text'] = df['text'].apply(lambda x: x.replace('-', '') if x[-1] == '-' else x)
    return df



print(ImageToText(im))

