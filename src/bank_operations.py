from typing import List, Dict, Any


def filter_by_status(data: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу.
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
    """
    valid_statuses = ['executed', 'canceled', 'pending']
    return status.lower() in valid_statuses


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """
    Выводит транзакции в читаемом формате.
    """
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nНайдено транзакций: {len(transactions)}")
    print("=" * 60)

    for i, transaction in enumerate(transactions, 1):
        date = transaction.get('date', 'Неизвестная дата')
        description = transaction.get('description', 'Без описания')
        amount = transaction.get('amount', 0)
        currency = transaction.get('currency', '')
        status = transaction.get('status', 'Неизвестен')

        print(f"{i}. Дата: {date}")
        print(f"   Описание: {description}")
        print(f"   Сумма: {amount} {currency}")
        print(f"   Статус: {status}")
        print("-" * 40)
