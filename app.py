from flask import Flask, render_template, request
from database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database ကို စတင်ခေါ်ခြင်း
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    return f"Analyzing {video_url}..."

if __name__ == '__main__':
    app.run(debug=True)