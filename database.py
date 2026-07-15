from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./clipgenie.db"

# Engine တည်ဆောက်ခြင်း
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session တည်ဆောက်ခြင်း
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class (Table တွေ အားလုံးက ဒီ Base ကနေ ဆင်းသက်လာမှာပါ)
Base = declarative_base()

# Database နဲ့ ချိတ်ဆက်ဖို့ Dependency Function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()