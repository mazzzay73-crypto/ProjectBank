import pytest
import sys
import os
from unittest.mock import patch, Mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    import src.external_api as api_module

    get_transaction_amount_in_rub = api_module.get_transaction_amount_in_rub
    convert_to_rub = api_module.convert_to_rub
    get_exchange_rates = api_module.get_exchange_rates
except ImportError:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
    from src.external_api import (
        get_transaction_amount_in_rub,
        convert_to_rub,
        get_exchange_rates
    )


def test_convert_rub_to_rub():
    """Тест: рубли в рубли"""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = convert_to_rub(transaction)
    assert result == 100.0


@patch('src.external_api.requests.get')
def test_convert_usd_to_rub(mock_get):
    """Тест: доллары в рубли"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'success': True,
        'query': {'from': 'USD', 'to': 'RUB', 'amount': 100.0},
        'info': {'rate': 75.5},
        'result': 7550.0
    }
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = convert_to_rub(transaction)
    assert result == 7550.0

    mock_get.assert_called_once()
    call_args = mock_get.call_args
    url = call_args[0][0]
    params = call_args[1]['params']
    headers = call_args[1]['headers']

    assert 'convert' in url
    assert params['from'] == 'USD'
    assert params['to'] == 'RUB'
    assert float(params['amount']) == 100.0
    assert 'apikey' in headers


@patch('src.external_api.requests.get')
def test_convert_eur_to_rub(mock_get):
    """Тест: евро в рубли"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'success': True,
        'result': 8200.0
    }
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "EUR"
            }
        }
    }

    result = convert_to_rub(transaction)
    assert result == 8200.0


def test_get_transaction_amount_rub():
    """Тест основной функции с рублями"""
    transaction = {
        "id": 1,
        "operationAmount": {
            "amount": "1000.0",
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = get_transaction_amount_in_rub(transaction)
    assert result == 1000.0


@patch('src.external_api.convert_to_rub')
def test_get_transaction_amount_usd(mock_convert):
    """Тест основной функции с долларами"""
    mock_convert.return_value = 7500.0

    transaction = {
        "id": 2,
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = get_transaction_amount_in_rub(transaction)
    assert result == 7500.0
    mock_convert.assert_called_once_with(transaction)


@patch('src.external_api.requests.get')
def test_get_exchange_rates(mock_get):
    """Тест получения курсов валют"""
    mock_response = Mock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 0.011,
            'EUR': 0.010
        }
    }
    mock_get.return_value = mock_response

    rates = get_exchange_rates('RUB')

    assert 'USD' in rates
    assert 'EUR' in rates
    assert rates['USD'] == 0.011
    assert rates['EUR'] == 0.010


if __name__ == '__main__':
    pytest.main([__file__, "-v"])