import webbrowser
import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
from generate_html import *

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

    im = Image.open("1.png")

    data = pytesseract.image_to_data(im, output_type='dict')
    boxes = len(data['level'])
    text = pytesseract.image_to_string(im)    
    generate_html("testpage", text)