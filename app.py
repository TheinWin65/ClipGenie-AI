from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    # ဒီနေရာမှာ History Page ကို ပြသဖို့ render_template သုံးနိုင်ပါတယ်
    # အခုလောလောဆယ်တော့ အလုပ်လုပ်မလုပ် စမ်းသပ်ဖို့ စာသားလေးပဲ အရင်ထုတ်ပြထားပါတယ်
    return "<h1>History Page အောင်မြင်စွာ ရောက်ရှိပါပြီ</h1>"

@app.route('/new_chat')
def new_chat():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)