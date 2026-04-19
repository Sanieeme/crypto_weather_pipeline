import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch crypto data")

    return response.json()