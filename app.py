import os
import base64
import io
from flask import Flask, render_template, request
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/photo-edit', methods=['GET', 'POST'])
def photo_edit():
    result_image_b64 = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            input_image = Image.open(file)
            # AI နောက်ခံဖျက်ခြင်း
            output_image = remove(input_image)
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            result_image_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return render_template('photo_edit.html', result_image=result_image_b64)

if __name__ == '__main__':
    app.run()