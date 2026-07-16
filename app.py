from flask import Flask, render_template, request
from database import db, init_db, User
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database စတင်ခြင်း
init_db(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    if not video_url:
        return "လင့်ခ်တစ်ခုခု ထည့်ပေးပါခင်ဗျာ။"
    
    try:
        # YouTube URL ထဲက ID ကို ဖြတ်ယူခြင်း
        # ဥပမာ - https://www.youtube.com/watch?v=XXXXX ဆိုရင် XXXXX ကို ယူတာပါ
        video_id = video_url.split("v=")[-1]
        
        # Transcript ထုတ်ယူခြင်း
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # စာသားတွေကို ပေါင်းပေးခြင်း
        full_text = " ".join([item['text'] for item in transcript])
        
        # AI ရလဒ် ပြသခြင်း
        return f"<h1>အောင်မြင်ပါသည်!</h1><p>ဗီဒီယိုအနှစ်ချုပ် စာသားများ ရရှိပါပြီ။</p><p>{full_text[:500]}...</p><a href='/'>နောက်ထပ်လုပ်ရန်</a>"
    
    except Exception as e:
        return f"အမှားဖြစ်ပွားနေပါသည် (ဗီဒီယိုမှာ Transcript မပါတာလည်း ဖြစ်နိုင်ပါတယ်): {str(e)}"

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)