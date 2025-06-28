# app.py
from flask import Flask, render_template, request
import pyperclip
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    text_input = ''
    result = ''
    short_url = ''
    if request.method == 'POST':
        text_input = request.form.get('text')
        if text_input.strip():
            lines = text_input.strip().split('\n')
            words = text_input.strip().split()
            chars = list(text_input.strip())

            line_count = len(lines)
            word_count = len(words)
            char_count = len(chars)

            result = f"Lines: {line_count} | Words: {word_count} | Characters: {char_count}"
            pyperclip.copy(result)

           
    return render_template('index.html', text_input=text_input, result=result, short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
