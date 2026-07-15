import sqlite3

# Database ဖိုင်ကို ချိတ်ဆက်ခြင်း
conn = sqlite3.connect('clipgenie.db')
cursor = conn.cursor()

# Table ရှိမရှိ စစ်ဆေးခြင်း
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Database ထဲမှာရှိတဲ့ Tables များ:", tables)

conn.close()