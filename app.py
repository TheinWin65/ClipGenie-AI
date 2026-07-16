from flask import Flask, render_template, request
from database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video-gen')
def video_gen():
    return "<h1>AI Video Generation Page</h1><p>ဒီမှာ ဗီဒီယိုဖန်တီးတဲ့အပိုင်း ဖြစ်လာပါမယ်။</p>"

@app.route('/photo-edit')
def photo_edit():
    return "<h1>AI Photo Editing Page</h1><p>ဒီမှာ ပုံပြင်ဆင်တဲ့အပိုင်း ဖြစ်လာပါမယ်။</p>"

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    return f"Analyzing {video_url}..."

if __name__ == '__main__':
    app.run(debug=True)