import pytest
import json
from src.utils import load_transactions
from unittest.mock import mock_open, patch, MagicMock


# Тест 1: Файл не существует
def test_file_not_found_returns_empty_list():
    """Тест: возвращает пустой список если файл не существует"""
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False

        result = load_transactions('/path/to/nonexistent/file.json')

        assert result == []
        mock_exists.assert_called_once_with('/path/to/nonexistent/file.json')


# Тест 2: Пустой файл
def test_empty_file_returns_empty_list():
    """Тест: возвращает пустой список если файл пустой"""
    with patch('os.path.exists') as mock_exists, \
            patch('os.path.getsize') as mock_getsize:
        mock_exists.return_value = True
        mock_getsize.return_value = 0

        result = load_transactions('/path/to/empty/file.json')

        assert result == []
        mock_exists.assert_called_once_with('/path/to/empty/file.json')
        mock_getsize.assert_called_once_with('/path/to/empty/file.json')


# Тест 3: Корректный JSON со списком транзакций
def test_valid_json_list_returns_data():
    """Тест: возвращает данные если JSON содержит корректный список"""
    test_data = [
        {"id": 1, "amount": 100, "currency": "RUB"},
        {"id": 2, "amount": 50, "currency": "USD", "date": "2023-01-01"}
    ]

    with patch('os.path.exists') as mock_exists, \
            patch('os.path.getsize') as mock_getsize, \
            patch('builtins.open', mock_open()) as mock_file, \
            patch('json.load') as mock_json_load:
        mock_exists.return_value = True
        mock_getsize.return_value = 100
        mock_json_load.return_value = test_data

        result = load_transactions('/path/to/valid/file.json')

        assert result == test_data
        assert len(result) == 2
        assert result[0]['id'] == 1
        assert result[1]['currency'] == 'USD'

        mock_exists.assert_called_once_with('/path/to/valid/file.json')
        mock_getsize.assert_called_once_with('/path/to/valid/file.json')
        mock_file.assert_called_once_with('/path/to/valid/file.json', 'r', encoding='utf-8')


# Тест 4: JSON не является списком
def test_json_not_list_returns_empty_list():
    """Тест: возвращает пустой список если JSON не является списком"""
    with patch('os.path.exists') as mock_exists, \
            patch('os.path.getsize') as mock_getsize, \
            patch('builtins.open', mock_open()), \
            patch('json.load') as mock_json_load:
        mock_exists.return_value = True
        mock_getsize.return_value = 100
        mock_json_load.return_value = {"not": "a list"}  # Словарь вместо списка

        result = load_transactions('/path/to/invalid/file.json')

        assert result == []
        mock_exists.assert_called_once_with('/path/to/invalid/file.json')


# Тест 5: Некорректный JSON (синтаксическая ошибка)
def test_invalid_json_returns_empty_list():
    """Тест: возвращает пустой список если JSON некорректен"""
    with patch('os.path.exists') as mock_exists, \
            patch('os.path.getsize') as mock_getsize, \
            patch('builtins.open', mock_open()), \
            patch('json.load') as mock_json_load:
        mock_exists.return_value = True
        mock_getsize.return_value = 100
        mock_json_load.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)

        result = load_transactions('/path/to/broken/file.json')

        assert result == []
        mock_exists.assert_called_once_with('/path/to/broken/file.json')

