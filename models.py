import sqlite3

def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, user_message TEXT, ai_response TEXT)''')
    conn.commit()
    conn.close()

def save_message(user_msg, ai_res):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (user_message, ai_response) VALUES (?, ?)', (user_msg, ai_res))
    conn.commit()
    conn.close()

init_db()
import sqlite3

def init_db():
    conn = sqlite3.connect('clipgenie.db')
    cursor = conn.cursor()
    # User ဇယား ဆောက်မယ်
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY, username TEXT, credit INTEGER)''')
    
    # စမ်းသပ်ဖို့ User တစ်ယောက် ထည့်မယ် (အကယ်၍ မရှိရင်)
    cursor.execute("INSERT OR IGNORE INTO users (id, username, credit) VALUES (1, 'Admin', 100)")
    
    conn.commit()
    conn.close()

# အခုပဲ Database ကို စတင်ဆောက်ပေးပါ
init_db()