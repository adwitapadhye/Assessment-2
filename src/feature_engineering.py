import pandas as pd

def engineer_features(df):
    df = df.sort_values("timestamp")

    # User transaction count
    df["user_txn_count"] = df.groupby("user_id").cumcount() + 1

    # Avg amt spent by user till now
    df["user_avg_amt"] = (
        df.groupby("user_id")["amt"]
        .expanding()
        .mean()
        .reset_index(level=0, drop=True)
    )

    # Amt deviation from the original
    df["amt_deviation"] = df["amt"] / (df["user_avg_amt"] + 1)

    # Device sharing
    device_user_count = df.groupby("device_id")["user_id"].nunique()
    df["device_user_count"] = df["device_id"].map(device_user_count)

    # Convert categorical columns 
    df = pd.get_dummies(
        df,
        columns=["location", "payment_method"],
        drop_first=True
    )

    return df
