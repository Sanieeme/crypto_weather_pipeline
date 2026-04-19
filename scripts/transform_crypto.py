import pandas as pd
from datetime import datetime

def transform_crypto(data):
    records = []

    for coin, value in data.items():
        records.append({
            "coin": coin,
            "price": value["usd"],
            "timestamp": datetime.now()
        })

    return pd.DataFrame(records)