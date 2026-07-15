import sqlite3

def reset_credit():
    conn = sqlite3.connect('clipgenie.db')
    cursor = conn.cursor()
    # Credit ကို 100 ဖြစ်အောင် ပြန်ပြင်မယ်
    cursor.execute("UPDATE users SET credit = 100 WHERE id = 1")
    conn.commit()
    print("Credit ကို 100 သို့ အောင်မြင်စွာ ပြန်ဖြည့်လိုက်ပါပြီ။")
    conn.close()

if __name__ == '__main__':
    reset_credit()