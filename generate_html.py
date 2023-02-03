import webbrowser
import pandas as pd
import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def linebreak(txt = str):
    """
    This function detect systematic errors and rectifies them.
    """
    pattern = [['—\s', ' '], ['‘‘\s','"'], ['\s‘‘','"'], ['-\s', ' ']]
    for i in pattern:
        txt = re.sub(i[0], i[1], txt)
    return txt

def ImagePreProcess(im):
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    return im

im = Image.open("1.png")
im = ImagePreProcess(im)

def ImageToText(im):
    data = pytesseract.image_to_data(im, output_type='data.frame')
    df = pd.DataFrame(data)
    df.dropna(subset=['text'], inplace=True)
    df.reset_index(inplace=True)
    df['text'].apply(linebreak)
    df['text'] = df['text'].apply(lambda x: x.replace('-', '') if x[-1] == '-' else x)
    return df

def generate_html(file_name: str, output=None) -> None:
    df = ImageToText(im)
    f = open(f"{file_name}.html", "w")

    words = df[["par_num", "text"]]
    output = ["<p>"]
    current_paragraph = 1
    for index, word in words.iterrows():
        if df.iloc[index]["par_num"] != current_paragraph: #if paragraph number changes
            output.extend(["</p>", "<p>", word["text"]])
            current_paragraph += 1
        else:
            output.append(word["text"])
    output = ' '.join(output)

    # replace characters not encoded in UTF-8
    output = output.replace("“", "\"")
    output = output.replace("”", "\"")
    output = output.replace("’", "'")
    output = output.replace("‘", "'")
    output = output.replace("—‘", "-")
    output = output.replace("«", "\"")

    html = f"""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>{file_name}</title>
            <style>
                h2 {{text-align: center}}
                p {{margin-left: 20%; margin-right: 20%; text-align: justify}}
            </style>
        </head>
        <body>
            <h2>New page</h2>

            {output}

        </body>
    </html>
    """

    f.write(html)
    f.close()
    webbrowser.open_new_tab(f"{file_name}.html")