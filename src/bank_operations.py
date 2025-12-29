from typing import List, Dict, Any


def filter_by_status(data: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу.

    Args:
        data: Список словарей с данными о транзакциях
        status: Статус для фильтрации

    Returns:
        Отфильтрованный список транзакций
    """
    if not data:
        return []

    status_lower = status.lower()
    filtered_data = []

    for item in data:
        item_status = item.get('status', '').lower()
        if item_status == status_lower:
            filtered_data.append(item)

    return filtered_data


def validate_status(status: str) -> bool:
    """
    Проверяет, является ли статус допустимым.

    Args:
        status: Статус для проверки

    Returns:
        True если статус допустим, False в противном случае
    """
    valid_statuses = ['executed', 'canceled', 'pending']
    return status.lower() in valid_statuses


def format_transaction(transaction: Dict[str, Any]) -> str:
    """
    Форматирует транзакцию для вывода.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Отформатированная строка
    """
    date = transaction.get('date', 'Неизвестная дата')
    description = transaction.get('description', 'Без описания')
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', '')
    status = transaction.get('status', 'Неизвестен')

    return f"{date} | {description} | {amount} {currency} | {status}"
