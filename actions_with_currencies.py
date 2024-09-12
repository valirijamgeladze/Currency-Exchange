import requests
import config

def get_exchanged_cur(initial_currency, target_currency, amount, api_key = config.API_KEY):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{initial_currency}/{target_currency}/{amount}"
    data = requests.get(url).json()
    return data
