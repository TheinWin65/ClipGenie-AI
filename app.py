import os
import base64
import io
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from rembg import remove
from PIL import Image

app = Flask(__name__)
# Database Path ကို Render အတွက် အမှန်ပြင်ထားသည်
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'clipgenie.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    credit = db.Column(db.Integer, default=50)

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        db.session.add(User(username='admin', password='password123', credit=50))
        db.session.commit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/photo-edit', methods=['GET', 'POST'])
def photo_edit():
    result_image_b64 = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            input_image = Image.open(file)
            output_image = remove(input_image)
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            result_image_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return render_template('photo_edit.html', result_image=result_image_b64)

if __name__ == '__main__':
    app.run()