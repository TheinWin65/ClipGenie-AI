from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Database ထဲမှာ အသုံးပြုသူ ကြိုတင်ထည့်ပေးမည့် စနစ်
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        new_user = User(username='admin', password='123', credit=50)
        db.session.add(new_user)
        db.session.commit()

@app.route('/')
def index():
    # ပထမဆုံးဝင်ရင် Login ဝင်ဖို့ ခလုတ်ပဲပြမယ်
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            # Login အောင်မြင်ရင် Dashboard ကို ပို့ပေးမယ်
            return redirect(url_for('dashboard'))
        else:
            return "Username သို့မဟုတ် Password မှားယွင်းနေပါသည်။"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Login ဝင်ပြီးသူအတွက် Dashboard ပြပေးမယ်
    user = User.query.filter_by(username='admin').first()
    return render_template('dashboard.html', credit=user.credit)

@app.route('/analyze', methods=['POST'])
def analyze():
    # YouTube Link ကို ဒီနေရာမှာ ဖမ်းယူပြီး AI အလုပ်လုပ်ပါမယ်
    return "Analyzing video..."

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

if __name__ == '__main__':
    app.run(debug=True)