from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    # ဤနေရာတွင် Database မှ Data များကို နောက်မှ ဆက်လက်ချိတ်ဆက်ပါမည်
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)