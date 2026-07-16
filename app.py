from flask import Flask, render_template, request
from database import db, init_db

app = Flask(__name__)
# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database စတင်အသုံးပြုခြင်း
init_db(app)

# Routes များ
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video-gen')
def video_gen():
    return render_template('video_gen.html')

@app.route('/photo-edit')
def photo_edit():
    return render_template('photo_edit.html')

@app.route('/history')
def history():
    # နောက်ပိုင်းတွင် User ၏ လုပ်ဆောင်ချက် မှတ်တမ်းများကို Database မှ ဆွဲထုတ်ပြပါမည်
    return "ဤနေရာတွင် အသုံးပြုသူ၏ မှတ်တမ်းများ ပေါ်လာပါမည်။"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Database စစ်ဆေးခြင်း Logic ကို နောက်တစ်ဆင့်မှာ ဆက်ရေးပါမယ်
        return f"လှိုက်လှဲစွာကြိုဆိုပါတယ် {username}၊ Login အောင်မြင်ပါသည်!"
    return render_template('login.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    # နောက်ပိုင်းတွင် YouTube Transcript API နှင့် ချိတ်ဆက်ပါမည်
    return f"လင့်ခ် {video_url} ကို ခွဲခြမ်းစိတ်ဖြာနေပါသည်..."

if __name__ == '__main__':
    app.run(debug=True)