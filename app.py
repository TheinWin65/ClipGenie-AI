from flask import Flask, render_template, request
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Database မှ User ရဲ့ Credit ကို ဆွဲထုတ်ခြင်း
    user = User.query.first() 
    credit_value = user.credit if user else 0
    return render_template('index.html', credit=credit_value)

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

@app.route('/history')
def history():
    return "မှတ်တမ်းများ ဤနေရာတွင် ပေါ်လာပါမည်။"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    return "Analyzing video..."

if __name__ == '__main__':
    app.run(debug=True)