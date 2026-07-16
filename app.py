from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Database ထဲမှာ Test User ကြိုထည့်ပေးမည့် အပိုင်း
def init_db_data():
    with app.app_context():
        db.create_all()
        # User မရှိသေးရင်ပဲ ထည့်မယ်
        if not User.query.filter_by(username='admin').first():
            test_user = User(username='admin', password='123', credit=50)
            db.session.add(test_user)
            db.session.commit()

init_db_data() # အပေါ်က function ကို ခေါ်လိုက်တာပါ

@app.route('/')
def index():
    # လက်ရှိမှာ admin ဆိုတဲ့ user ကိုပဲ ပြထားတာပါ
    user = User.query.filter_by(username='admin').first()
    credit_value = user.credit if user else 0
    return render_template('index.html', credit=credit_value)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            return f"Login အောင်မြင်ပါသည်! ဆရာ့ Credit မှာ {user.credit} ကျန်ရှိပါသည်။"
        else:
            return "Username သို့မဟုတ် Password မှားယွင်းနေပါသည်။"
    return render_template('login.html')

# ... (အခြား route များ)