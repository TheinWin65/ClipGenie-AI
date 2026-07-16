import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Folder များ သတ်မှတ်ခြင်း
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    credit = db.Column(db.Integer, default=50)

# Folder များ ရှိမရှိ စစ်ဆေးပြီး ဆောက်ပေးခြင်း
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

with app.app_context():
    db.create_all()             
    # အမြဲ Login ဝင်နိုင်ရန် Admin User ထည့်ပေးခြင်း
    if not User.query.filter_by(username='admin').first():
        db.session.add(User(username='admin', password='password123', credit=50))
        db.session.commit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return redirect(url_for('dashboard'))
    return "Login အဆင်မပြေပါ"

@app.route('/dashboard')
def dashboard():
    user = User.query.filter_by(username='admin').first()
    return render_template('dashboard.html', credit=user.credit if user else 0)

@app.route('/photo-edit', methods=['GET', 'POST'])
def photo_edit():
    result_image = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # ပုံကို သိမ်းမယ်
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # AI နောက်ခံဖျက်ခြင်း
            input_image = Image.open(filepath)
            output_image = remove(input_image)
            
            # ဖိုင်နာမည်သတ်မှတ်ပြီး သိမ်းမယ်
            result_filename = "processed_" + file.filename
            output_image.save(os.path.join(app.config['PROCESSED_FOLDER'], result_filename))
            result_image = result_filename
            
    return render_template('photo_edit.html', result_image=result_image)

if __name__ == '__main__':
    app.run(debug=True)