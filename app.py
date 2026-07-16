from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Database ထဲမှာ user ရှိမရှိ စစ်ဆေးပြီး ထည့်ပေးခြင်း
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        new_user = User(username='admin', password='123', credit=50)
        db.session.add(new_user)
        db.session.commit()

@app.route('/')
def index():
    # ၁။ ပထမဆုံးဝင်လာရင် Login စာမျက်နှာကိုပဲ ပြမယ်
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # ၂။ Login ဝင်ပြီးသွားရင် Dashboard ကို ပို့မယ်
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        return redirect(url_for('dashboard')) # အောင်မြင်ရင် Dashboard သွား
    else:
        return "Username သို့မဟုတ် Password မှားယွင်းနေပါသည်။"

@app.route('/dashboard')
def dashboard():
    # ၃။ Dashboard မှာမှ မီနူးတွေနဲ့ လုပ်စရာတွေကို ပြမယ်
    user = User.query.filter_by(username='admin').first()
    return render_template('dashboard.html', credit=user.credit)

# ကျန်တဲ့ route များ (analyze, video-gen စသည်) ကိုလည်း ဤအတိုင်း ဆက်ရေးပါ