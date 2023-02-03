import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import pandas as pd
import re
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def ImagePreProcess(im):
    #im = im.filter(ImageFilter.MedianFilter())
    #enhancer = ImageEnhance.Contrast(im)
    #im = enhancer.enhance(2)
    #im = im.convert('1')
    im.show()
    return im

im = Image.open("1.png")
im = ImagePreProcess(im)

def linebreak(txt : str):
    """
    This function detect systematica errors and rectify them
    """
    pattern = [['—\s', ' '], ['‘‘\s','"'], ['\s‘‘','"'], ['-\s', ' ']]
    for i in pattern:
        txt = re.sub(i[0], i[1], txt)
    return txt

def word_concat(df : pd.DataFrame):

    df_text = df['text']
    index_to_replace = np.array(df_text.index[df_text.str.findall('-$').str.len() != 0].tolist())
    index_to_drop = index_to_replace + 1 
    sub = []

    for item in index_to_drop:
        sub.append(df['text'][item])

    df.drop(index = index_to_drop, inplace = True)

    for index, item in enumerate(index_to_replace):
        df['text'][item] = df['text'][item][:-1] + sub[index]

    return df


def ImageToText(im):
    data = pytesseract.image_to_data(im, output_type='data.frame')
    df = pd.DataFrame(data)
    df.dropna(subset=['text'], inplace=True)
    df.reset_index(inplace=True)
    # df['text'].apply(linebreak)
    # df['text'] = df['text'].apply(lambda x: x.replace('-', '') if x[-1] == '-' else x)
    word_concat(df)
    #df.to_csv("test.csv")
    #print(pytesseract.image_to_string(im))
    #return df.head(20)
    return df





print(ImageToText(im))

