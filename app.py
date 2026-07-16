import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ဓာတ်ပုံသိမ်းမည့်နေရာ
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

db.init_app(app)

# Folder များ ရှိမရှိ စစ်ဆေးပြီး ဆောက်ပေးခြင်း
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

with app.app_context():
    db.create_all()

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
           # ပုံကို ဖတ်မယ်
            input_image = Image.open(file)
            # AI နဲ့ နောက်ခံဖျက်မယ်
            output_image = remove(input_image)
            
            # ဖိုင်ကို သိမ်းမယ်
            result_filename = "processed_" + file.filename
            output_image.save(os.path.join(app.config['PROCESSED_FOLDER'], result_filename))
            result_image = result_filename 
            
    return render_template('photo_edit.html', result_image=result_image)

@app.route('/analyze', methods=['POST'])
def analyze():
    return "Analyzing video..."

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

if __name__ == '__main__':
    app.run(debug=True)