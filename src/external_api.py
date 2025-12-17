import os
import requests
from typing import Dict, Any
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


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли через API endpoint /convert
    """
    api_key = os.getenv('API_KEY')

    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']
    except (KeyError, ValueError) as e:
        raise ValueError(f"Некорректная структура транзакции: {e}")

    if currency == 'RUB':
        return amount

    url = "https://api.apilayer.com/exchangerates_data/convert"

    params = {
        'from': currency,
        'to': 'RUB',
        'amount': amount
    }

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200 and data.get('success', False):
        result = data.get('result')
        if result is not None:
            return float(result)
        else:
            raise ValueError("API не вернул результат конвертации")
    else:
        error_info = data.get('error', {}).get('info', 'Неизвестная ошибка')
        raise ConnectionError(f"Ошибка API: {error_info}")


def get_transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях
    """
    return convert_to_rub(transaction)
