from flask import Flask, render_template, request
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Database ထဲမှာ Test User ကြိုထည့်ပေးမည့်စနစ်
def init_db_data():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            test_user = User(username='admin', password='123', credit=50)
            db.session.add(test_user)
            db.session.commit()

init_db_data()

@app.route('/')
def index():
    # Home page မှာ လက်ရှိ Test User (admin) ရဲ့ Credit ကို ပြပေးမယ်
    user = User.query.filter_by(username='admin').first()
    credit = user.credit if user else 0
    return render_template('index.html', credit=credit)

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

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

@app.route('/history')
def history():
    return "မှတ်တမ်းများ ဤနေရာတွင် ပေါ်လာပါမည်။"

if __name__ == '__main__':
    app.run(debug=True)