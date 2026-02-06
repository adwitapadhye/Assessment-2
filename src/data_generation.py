import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta


def generate_transactions(
    n_users=1000,
    n_merchants=300,
    n_transactions=15000,
    start_date=datetime(2024, 1, 1)
):
    users = [f"user_{i}" for i in range(n_users)]
    merchants = [f"merchant_{i}" for i in range(n_merchants)]
    payment_methods = ["credit_card", "debit_card", "upi", "wallet"]
    locations = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]

    transactions = []
    current_time = start_date

    for i in range(n_transactions):
        amount = max(50, round(np.random.exponential(scale=1200), 2))
        transactions.append({
            "transaction_id": f"tx_{i}",
            "user_id": random.choice(users),
            "merchant_id": random.choice(merchants),
            "amount": amount,
            "timestamp": current_time,
            "location": random.choice(locations),
            "payment_method": random.choice(payment_methods),
            "device_id": f"device_{random.randint(1, 3000)}",
            "is_fraud": 0
        })
        current_time += timedelta(minutes=random.randint(1, 8))
    return pd.DataFrame(transactions)
