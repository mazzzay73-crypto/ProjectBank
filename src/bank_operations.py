from typing import List, Dict, Any


def filter_by_status(data: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу.
    """
    if not data:
        return []

    status_lower = status.lower()
    result = []

    for item in data:
        item_status = item.get('status', '').lower()
        if item_status == status_lower:
            result.append(item)

    return result


def validate_status(status: str) -> bool:
    """
    Проверяет, является ли статус допустимым.
    """
    valid_statuses = ['executed', 'canceled', 'pending']
    return status.lower() in valid_statuses


def filter_rub_transactions(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Фильтрует только рублевые транзакции.
    """
    if not data:
        return []

    rub_currencies = ['RUB', 'RUR', 'РУБ']
    return [item for item in data if item.get('currency', '').upper() in rub_currencies]


def sort_by_date(data: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате.
    """
    if not data:
        return []

    def get_date(item):
        return item.get('date', '')

    return sorted(data, key=get_date, reverse=not ascending)


def format_transaction(transaction: Dict[str, Any]) -> str:
    """
    Форматирует транзакцию для вывода.
    """
    date = transaction.get('date', 'Неизвестно')
    description = transaction.get('description', 'Без описания')
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', '')
    status = transaction.get('status', 'Неизвестен')

    return f"{date} | {description} | {amount} {currency} | {status}"
