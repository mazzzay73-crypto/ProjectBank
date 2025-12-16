import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rates(base_currency: str = 'RUB') -> Dict[str, float]:
    """
    Получает текущие курсы валют от API
    """
    api_key = os.getenv('API_KEY')

    url = "https://api.apilayer.com/exchangerates_data/latest"

    params = {
        'base': base_currency
    }

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    return data.get('rates', {})


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму в рубли
    """
    if currency == 'RUB':
        return amount

    rates = get_exchange_rates('RUB')

    rate = rates.get(currency)

    if rate:
        result = amount / rate
        return round(result, 2)
    else:
        raise ValueError(f"Курс для валюты {currency} не найден")


def get_transaction_amount_in_rub(transaction: tuple) -> float:
    """
    Возвращает сумму транзакции в рублях
    """
    amount, currency = transaction
    return convert_to_rub(amount, currency)


import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rates(base_currency: str = 'RUB') -> Dict[str, float]:
    """
    Получает текущие курсы валют от API
    """
    api_key = os.getenv('API_KEY')

    url = "https://api.apilayer.com/exchangerates_data/latest"

    params = {
        'base': base_currency
    }

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    return data.get('rates', {})


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму в рубли
    """
    if currency == 'RUB':
        return amount

    rates = get_exchange_rates('RUB')

    rate = rates.get(currency)

    if rate:
        result = amount / rate
        return round(result, 2)
    else:
        raise ValueError(f"Курс для валюты {currency} не найден")


def get_transaction_amount_in_rub(transaction: tuple) -> float:
    """
    Возвращает сумму транзакции в рублях
    """
    amount, currency = transaction
    return convert_to_rub(amount, currency)
