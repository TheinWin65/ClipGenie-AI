from flask import Flask, render_template, request
from database import db, init_db, User

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database ကို စတင်ခေါ်ခြင်း
init_db(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    if video_url:
        # ဒီနေရာမှာ AI နဲ့ လုပ်ဆောင်ချက်တွေကို နောက်မှ ထည့်သွင်းမှာပါ
        return f"ဗီဒီယို {video_url} ကို AI နဲ့ ခွဲခြမ်းစိတ်ဖြာနေပါပြီ... ခဏစောင့်ပေးပါ။"
    return "လင့်ခ်တစ်ခုခု ထည့်ပေးဖို့ လိုပါတယ်!"

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)