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
    result = convert_to_rub(100.0, 'RUB')
    assert result == 100.0


@patch('src.external_api.requests.get')
def test_convert_usd_to_rub(mock_get):
    """Тест: доллары в рубли"""
    mock_response = Mock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 0.011,  # 1 RUB = 0.011 USD
            'EUR': 0.010
        }
    }
    mock_get.return_value = mock_response

    result = convert_to_rub(100.0, 'USD')

    assert result == pytest.approx(9090.91, rel=0.01)


@patch('src.external_api.requests.get')
def test_convert_eur_to_rub(mock_get):
    """Тест: евро в рубли"""
    mock_response = Mock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 0.011,
            'EUR': 0.010  # 1 RUB = 0.010 EUR
        }
    }
    mock_get.return_value = mock_response

    result = convert_to_rub(50.0, 'EUR')

    assert result == pytest.approx(5000.0, rel=0.01)


@patch('src.external_api.requests.get')
def test_convert_currency_not_found(mock_get):
    """Тест: валюта не найдена"""
    mock_response = Mock()
    mock_response.json.return_value = {
        'rates': {
            'USD': 0.011,
            'EUR': 0.010
        }
    }
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="не найден"):
        convert_to_rub(100.0, 'JPY')


def test_get_transaction_amount_rub():
    """Тест основной функции с рублями"""
    transaction = (1000.0, 'RUB')
    result = get_transaction_amount_in_rub(transaction)
    assert result == 1000.0


@patch('src.external_api.convert_to_rub')
def test_get_transaction_amount_usd(mock_convert):
    """Тест основной функции с долларами"""
    mock_convert.return_value = 7500.0

    transaction = (100.0, 'USD')
    result = get_transaction_amount_in_rub(transaction)

    assert result == 7500.0
    mock_convert.assert_called_once_with(100.0, 'USD')


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
    pytest.main([__file__])\
