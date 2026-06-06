from datetime import datetime, timedelta
import random
from pymongo import MongoClient

# ================================
# 🔥 ATLAS CONNECTION (PASTE YOUR URI HERE)
# ================================
client = MongoClient("mongodb+srv://Admin:FinalProject2026@admin.mjowyos.mongodb.net/finintelligence?retryWrites=true&w=majority")

db = client["finintelligence"]
collection = db["expenses"]

# ================================
# USERS
# ================================
users = [
    "nemi123@gmail.com",
    "ali123@gmail.com",
    "sara123@gmail.com"
]

# ================================
# CATEGORIES
# ================================
categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment"]

start_date = datetime(2026, 1, 1)

data = []

# ================================
# GENERATE DATA (150 EACH USER)
# ================================
for user in users:

    base_multiplier = random.uniform(0.8, 1.6)

    for i in range(150):

        date = start_date + timedelta(days=i // 3)

        category = random.choice(categories)

        if category == "Bills":
            amount = random.randint(1000, 4000)
        elif category == "Food":
            amount = random.randint(200, 1500)
        elif category == "Shopping":
            amount = random.randint(500, 5000)
        else:
            amount = random.randint(100, 2000)

        amount = int(amount * base_multiplier)

        data.append({
            "email": user,
            "title": f"{category} Expense {i+1}",
            "category": category,
            "amount": amount,
            "date": date.strftime("%Y-%m-%d")
        })

# ================================
# INSERT INTO MONGODB
# ================================
try:
    collection.insert_many(data)
    print("✅ 150 entries per user inserted successfully!")

except Exception as e:
    print("❌ Error:", str(e))