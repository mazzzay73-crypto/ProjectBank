def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает новый список словарей, содержащий словари, у которых ключ
state соответствует указанному значению."""
    filtered_list = []
    for item in list_dict:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(list_of_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей и возвращает список, отсортированный по дате"""
    sorted_list = sorted(list_of_dict, key=lambda item: item["date"], reverse=reverse)
    return sorted_list


list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


filtered = filter_by_state(list_dict, state="EXECUTED")
print(filtered)

list_of_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(sort_by_date)
