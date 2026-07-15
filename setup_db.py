import sqlite3

conn = sqlite3.connect('clipgenie.db')
cursor = conn.cursor()

# Chat History Table အသစ်ဆောက်မယ်
cursor.execute('''CREATE TABLE IF NOT EXISTS chat_history 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   user_id INTEGER, 
                   message TEXT, 
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()
conn.close()
print("Chat History Table အောင်မြင်စွာ တည်ဆောက်ပြီးပါပြီ။")