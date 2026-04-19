from db.init_db import create_tables

from scripts.extract_crypto import fetch_crypto_data
from scripts.transform_crypto import transform_crypto
from scripts.load_crypto import load_crypto

from scripts.extract_weather import fetch_weather_data
from scripts.transform_weather import transform_weather
from scripts.load_weather import load_weather


def run_pipeline():
    # Ensure tables exist
    create_tables()

    # Crypto ETL
    crypto_raw = fetch_crypto_data()
    crypto_clean = transform_crypto(crypto_raw)
    load_crypto(crypto_clean)

    # Weather ETL
    weather_raw = fetch_weather_data()
    weather_clean = transform_weather(weather_raw)
    load_weather(weather_clean)

    print("Pipeline ran successfully!")


if __name__ == "__main__":
    run_pipeline()