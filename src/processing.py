from datetime import datetime

def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    filtred_list = []
    for item in list_dict:
        if item.get("state") == state:
            filtred_list.append(item)
    return filtred_list


def sort_by_date(list_of_dict: list[dict], reverse=True) -> list[dict]:
    sorted_list = sorted(list_of_dict, key=lambda item: datetime.strptime(item["date"], "%Y-%m-%d"))
    return sorted_list


list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

filtred = filter_by_state(list_dict, state = "EXECUTED")
print(filtred)

list_of_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(sort_by_date)
