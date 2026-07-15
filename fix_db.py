import sqlite3
conn = sqlite3.connect('clipgenie.db')
cursor = conn.cursor()

# ၁။ User Table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, credit INTEGER)')
cursor.execute('INSERT OR IGNORE INTO users (id, username, credit) VALUES (1, "Admin", 100)')

# ၂။ History Table (အမှားမပါအောင် column အသစ်တွေနဲ့ ပြန်ဆောက်)
cursor.execute('DROP TABLE IF EXISTS chat_history')
cursor.execute('''CREATE TABLE chat_history 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   user_id INTEGER, 
                   message TEXT)''')

conn.commit()
conn.close()
print("Database နှင့် History Table ကို အမှားမပါအောင် ပြန်ပြင်ဆောက်ပြီးပါပြီ။")