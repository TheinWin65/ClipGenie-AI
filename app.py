from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import google.generativeai as genai

app = Flask(__name__)
DB_NAME = 'clipgenie.db'

# API Key ချိတ်ဆက်ခြင်း
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # AI ဆီက အဖြေကို တောင်းယူခြင်း
    try:
        response_data = model.generate_content(user_message)
        ai_text = response_data.text
    except Exception as e:
        ai_text = "AI အလုပ်မလုပ်ပါ (API Key စစ်ဆေးပါ)"

    return jsonify({"response": ai_text})

if __name__ == '__main__':
    app.run(debug=True)