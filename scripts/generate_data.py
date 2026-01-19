import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)  # Ensures the data is the same every time you run it

def generate_eco_data(num_rows=100):
    # Mapping Merchants to MCC and Carbon Factors
    categories = {
        "Airlines": {"mcc": 4511, "factor": 0.15, "merchants": ["Delta", "United", "Emirates"]},
        "Groceries": {"mcc": 5411, "factor": 0.02, "merchants": ["Whole Foods", "Tesco", "Walmart"]},
        "Dining": {"mcc": 5812, "factor": 0.05, "merchants": ["Starbucks", "McDonalds", "Local Cafe"]},
        "Transport": {"mcc": 4121, "factor": 0.08, "merchants": ["Uber", "Lyft", "Public Transit"]}
    }

    data = []
    for _ in range(num_rows):
        cat_name = random.choice(list(categories.keys()))
        cat_info = categories[cat_name]
        
        amount = round(random.uniform(5, 500), 2)
        co2_kg = round(amount * cat_info["factor"], 2)

        data.append({
            "transaction_id": fake.uuid4()[:8],
            "date": fake.date_between(start_date='-30d', end_date='today'),
            "merchant": random.choice(cat_info["merchants"]),
            "mcc_code": cat_info["mcc"],
            "amount_usd": amount,
            "co2e_kg": co2_kg
        })
    
    return pd.DataFrame(data)

# Generate and save
df = generate_eco_data(100)
df.to_csv("transactions_synthetic.csv", index=False)
print("Dataset generated successfully!")
