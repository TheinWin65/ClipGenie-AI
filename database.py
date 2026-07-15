from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# အသုံးပြုသူအတွက် Data Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    credits = db.Column(db.Integer, default=10)  # အသုံးပြုသူအသစ်ကို Credit 10 ပေးထားမယ်

# Database ကို စတင်ဖန်တီးပေးမည့် Function
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clipgenie.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Database ဖိုင်ကို အလိုအလျောက် တည်ဆောက်ပေးမယ်
        print("Database initialized successfully!")

# Credit လျှော့ချပေးမည့် လုပ်ဆောင်ချက် (နောက်ပိုင်း အသုံးဝင်ပါမယ်)
def deduct_credit(user_id, amount):
    user = User.query.get(user_id)
    if user and user.credits >= amount:
        user.credits -= amount
        db.session.commit()
        return True
    return False