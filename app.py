import os
import base64
import io
from flask import Flask, render_template, request
from rembg import remove
from PIL import Image

app = Flask(__name__)

# Main Route - ပထမဆုံးဝင်တဲ့အခါ login.html ပြပေးမယ်
@app.route('/')
def index():
    return render_template('login.html')

# Photo Edit Route
@app.route('/photo-edit', methods=['GET', 'POST'])
def photo_edit():
    result_image_b64 = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            input_image = Image.open(file)
            output_image = remove(input_image)
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            result_image_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return render_template('photo_edit.html', result_image=result_image_b64)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)