import requests


def fetch_prices(limit=100):
    url = (
        f'https://api.energidataservice.dk/dataset/DayAheadPrices'
        f'?limit={limit}'
        f'&sort=TimeDK%20desc'
        f'&filter={{"PriceArea":"DK1"}}'
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    records = data["records"]

    return records




