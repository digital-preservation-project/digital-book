import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import pandas as pd
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def ImagePreProcess(im):
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    #im.show()
    return im

im = Image.open("1.png")
im = ImagePreProcess(im)

def ImageToText(im):
    data = pytesseract.image_to_data(im, output_type='data.frame')
    df = pd.DataFrame(data)
    df.dropna(subset=['text'], inplace=True)
    df.reset_index(inplace=True)
    #df.to_csv("test.csv")
    #print(pytesseract.image_to_string(im))
    return df.head(20)

print(ImageToText(im))