from datetime import datetime


def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED'):
    """Функция принимает список словарей и возвращает новый список словарей, содержащий словари, у которых ключ
state соответствует указанному значению."""
    filtered_list = []
    if not any('state' in item for item in list_dict):
        return "Not found"
    for item in list_dict:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(list_of_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей и возвращает список, отсортированный по дате"""
    sorted_list = sorted(list_of_dict, key=lambda item: item.get("date"), reverse=reverse)
    return sorted_list
