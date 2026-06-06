from datetime import datetime, timedelta
import random
from pymongo import MongoClient

# ================================
# 🔥 ATLAS CONNECTION (UPDATE THIS)
# ================================
client = MongoClient(
    "mongodb+srv://Admin:FinalProject2026@admin.mjowyos.mongodb.net/finintelligence?retryWrites=true&w=majority"
)

# ================================
# DATABASE
# ================================
db = client["finintelligence"]
collection = db["expenses"]

# ================================
# CONFIG
# ================================
email = "zabo123@gmail.com"

categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment"]

start_date = datetime(2026, 1, 1)

data = []

# ================================
# GENERATE 150 ENTRIES
# ================================
for i in range(150):

    # 3 entries per day (realistic pattern)
    date = start_date + timedelta(days=i // 3)

    entry = {
        "email": email,
        "title": f"Expense {i+1}",
        "category": random.choice(categories),
        "amount": round(random.uniform(100, 5000), 2),
        "date": date.strftime("%Y-%m-%d")
    }

    data.append(entry)

# ================================
# INSERT INTO MONGODB ATLAS
# ================================
try:
    collection.insert_many(data)
    print("✅ 150 dummy entries successfully inserted into MongoDB Atlas!")

except Exception as e:
    print("❌ Error inserting data:", str(e))