import webbrowser
def generate_html(file_name, output=None):
    f = open(f"{file_name}.html", "w")

    html = f"""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
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