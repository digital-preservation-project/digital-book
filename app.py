import webbrowser
import pytesseract
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

def generate_html(file_name, output=None):
    f = open(f"{file_name}.html", "w")

    html = f"""<!DOCTYPE HTML>
    <html>
        <head>
            <title>Test Page</title>
        </head>
        <body>
            <h2>Hello world!</h2>

            <p>{output}.</p>

        </body>
    </html>
    """

    f.write(html)
    f.close()
    webbrowser.open_new_tab(f"{file_name}.html")

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

    im = Image.open("1.jpg")

    data = pytesseract.image_to_data(im, output_type='dict')
    boxes = len(data['level'])
    text = pytesseract.image_to_string(im)    
    generate_html("testpage", text)