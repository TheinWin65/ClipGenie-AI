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
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        # ဒီနေရာမှာ Video လင့်ခ်ကို လက်ခံပြီး AI နဲ့ အလုပ်လုပ်မယ့်နေရာဖြစ်လာမှာပါ
        print(f"Received URL: {video_url}")
        
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)