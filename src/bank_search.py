import re
from typing import List, Dict, Any


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по наличию строки в описании.

    Args:
        data: Список словарей с данными о банковских операциях
        search: Строка для поиска в описании

    Returns:
        Отфильтрованный список словарей
    """
    if not data or not search:
        return []

    result = []
    try:
        pattern = re.compile(re.escape(search), re.IGNORECASE)

        for item in data:
            description = item.get('description', '')
            if pattern.search(description):
                result.append(item)
    except re.error:
        return []

    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        data: Список словарей с данными о банковских операциях
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по каждой категории
    """
    if not data:
        return {}

    categories_lower = [cat.lower() for cat in categories]

    result = {category: 0 for category in categories}

    for item in data:
        description = item.get('description', '').lower()

        for i, cat_lower in enumerate(categories_lower):
            if cat_lower in description:
                result[categories[i]] += 1

    return result
