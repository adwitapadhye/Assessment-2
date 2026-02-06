import random
import numpy as np


def inject_fraud_patterns(df, fraud_rate=0.03):
    fraud_count = int(len(df) * fraud_rate)
    fraud_indices = df.sample(fraud_count, random_state=42).index

    df.loc[fraud_indices, "is_fraud"] = 1

    cities = df["location"].unique().tolist()

    for idx in fraud_indices:
        pattern = random.choice([
            "velocity",
            "amount_spike",
            "location_jump",
            "shared_device",
            "merchant_abuse"
        ])

        if pattern == "velocity":
            user = df.loc[idx, "user_id"]
            df.loc[idx:idx+4, "user_id"] = user

        elif pattern == "amount_spike":
            df.loc[idx, "amount"] *= random.randint(5, 12)

        elif pattern == "location_jump":
            df.loc[idx, "location"] = random.choice(
                [c for c in cities if c != df.loc[idx, "location"]]
            )

        elif pattern == "shared_device":
            df.loc[idx, "device_id"] = "shared_fraud_device"

        elif pattern == "merchant_abuse":
            merchant = df.loc[idx, "merchant_id"]
            df.loc[idx:idx+3, "merchant_id"] = merchant

    return df
