import webbrowser
import pandas as pd

def generate_html(file_name, output=None):
    df = pd.read_csv("test.csv")
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

    html = f"""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>{file_name}</title>
        </head>
        <body>
            <h2>Hello world!</h2>

            {output}

        </body>
    </html>
    """

    f.write(html)
    f.close()
    webbrowser.open_new_tab(f"{file_name}.html")