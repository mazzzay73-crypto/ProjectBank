import re
from typing import List, Dict, Any
from collections import Counter


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по наличию строки в описании.
    """
    if not data or not search:
        return []

    result = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    for item in data:
        description = item.get('description', '')
        if pattern.search(description):
            result.append(item)

    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям с использованием Counter.
    """
    if not data or not categories:
        return {}

    counter = Counter()

    for item in data:
        description = item.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1

    return dict(counter)
