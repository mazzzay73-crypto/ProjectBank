import pytest
from collections import Counter
from src.bank_search import process_bank_search, process_bank_operations
from src.bank_operations import filter_by_status, validate_status


# Общие тестовые данные
@pytest.fixture
def transactions():
    return [
        {"id": 1, "description": "Перевод другу", "status": "EXECUTED"},
        {"id": 2, "description": "Оплата интернета", "status": "EXECUTED"},
        {"id": 3, "description": "Покупка в магазине", "status": "CANCELED"},
        {"id": 4, "description": "Перевод за аренду", "status": "EXECUTED"},
    ]


# Тесты для process_bank_search
def test_search_found(transactions):
    result = process_bank_search(transactions, "перевод")
    assert len(result) == 2


def test_search_not_found(transactions):
    assert len(process_bank_search(transactions, "кредит")) == 0


def test_search_empty():
    assert process_bank_search([], "test") == []
    assert process_bank_search([{"id": 1}], "") == []


# Тесты для process_bank_operations
def test_operations_count(transactions):
    result = process_bank_operations(transactions, ["Перевод", "Оплата"])
    assert result["Перевод"] == 2
    assert result["Оплата"] == 1


def test_operations_no_match(transactions):
    result = process_bank_operations(transactions, ["Кредит"])
    assert result["Кредит"] == 0


def test_operations_empty():
    assert process_bank_operations([], ["Тест"]) == {}


# Тесты для filter_by_status
def test_filter_executed(transactions):
    result = filter_by_status(transactions, "EXECUTED")
    assert len(result) == 3


def test_filter_canceled(transactions):
    result = filter_by_status(transactions, "CANCELED")
    assert len(result) == 1


def test_filter_not_found(transactions):
    result = filter_by_status(transactions, "TEST")
    assert len(result) == 0


# Тесты для validate_status
def test_validate_correct():
    assert validate_status("EXECUTED") is True
    assert validate_status("executed") is True
    assert validate_status("CANCELED") is True
    assert validate_status("PENDING") is True


def test_validate_incorrect():
    assert validate_status("TEST") is False
    assert validate_status("") is False


# Параметризованные тесты
@pytest.mark.parametrize("search,expected_count", [
    ("перевод", 2),
    ("интернета", 1),
    ("магазин", 1),
    ("тест", 0),
])
def test_search_param(transactions, search, expected_count):
    result = process_bank_search(transactions, search)
    assert len(result) == expected_count


@pytest.mark.parametrize("status,expected_count", [
    ("EXECUTED", 3),
    ("executed", 3),
    ("CANCELED", 1),
    ("PENDING", 0),
])
def test_filter_param(transactions, status, expected_count):
    result = filter_by_status(transactions, status)
    assert len(result) == expected_count


@pytest.mark.parametrize("status,is_valid", [
    ("EXECUTED", True),
    ("executed", True),
    ("CANCELED", True),
    ("PENDING", True),
    ("TEST", False),
    ("", False),
])
def test_validate_param(status, is_valid):
    assert validate_status(status) == is_valid


def test_process_bank_operations_with_counter(transactions):
    """Подсчет операций с использованием Counter"""
    categories = ["Перевод", "Оплата", "Покупка"]
    result = process_bank_operations(transactions, categories)

    # Проверяем, что результат - это словарь
    assert isinstance(result, dict)

    # Проверяем правильность подсчета
    assert result["Перевод"] == 2
    assert result["Оплата"] == 1
    assert result["Покупка"] == 1


def test_process_bank_operations_empty_categories(transactions):
    """Подсчет с пустыми категориями"""
    result = process_bank_operations(transactions, [])
    assert result == {}


def test_process_bank_operations_empty_data():
    """Подсчет с пустыми данными"""
    result = process_bank_operations([], ["Перевод"])
    assert result == {}
