from flask import Flask, render_template, request
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database စတင်ခြင်း
db.init_app(app)

# Database ဖန်တီးခြင်း
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # ဥပမာအနေနဲ့ User တစ်ယောက်ရဲ့ Credit ကိုပြခြင်း
    user = User.query.first() # လက်ရှိ Login ဝင်ထားသူ (နောက်ပိုင်းမှ ပြင်ပါမည်)
    credit = user.credit if user else 0
    return render_template('index.html', credit=credit)

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"လှိုက်လှဲစွာကြိုဆိုပါတယ် {username}!"
    return render_template('login.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    return "Analyzing video..."

if __name__ == '__main__':
    app.run(debug=True)