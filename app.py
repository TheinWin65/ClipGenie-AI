import os
import io
import base64
from flask import Flask, render_template, request
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_image = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            input_image = Image.open(file)
            output_image = remove(input_image)
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            result_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return render_template('login.html', result_image=result_image)

if __name__ == '__main__':
    app.run()