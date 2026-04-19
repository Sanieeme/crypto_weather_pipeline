import pandas as pd
from datetime import datetime

def transform_weather(data):
    weather = data["current_weather"]

    record = {
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "timestamp": datetime.now()
    }

    return pd.DataFrame([record])