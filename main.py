from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router # routes.py ထဲက router ကို ခေါ်ပါတယ်
import models
import database

# Database ကို စတင်ဖန်တီးပေးခြင်း
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# CORS Middleware (Flutter ကနေ လှမ်းခေါ်ဖို့အတွက် လိုအပ်ပါတယ်)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes တွေကို Register လုပ်ပေးတာပါ
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "ClipGenieAI AI Engine အသင့်ရှိနေပါပြီ"}