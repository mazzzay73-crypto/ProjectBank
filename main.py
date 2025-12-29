from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.bank_search import process_bank_search, process_bank_operations
from src.bank_operations import filter_by_status, validate_status

card_number = input("Please enter card number: ")
masked_number = get_mask_card_number(card_number)
print(masked_number)

account_number = input("Please enter account number: ")
masked_account = get_mask_account(account_number)
print(masked_account)

date = input("Please enter date")
correct_day = get_date(date)
print(correct_day)

card_info = input("Please enter your number: ")
result = mask_account_card(card_info)
print(result)

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


sorted_list = sort_by_date(list_of_dict, reverse=True)
print(sorted_list)


def main():
    """Демонстрация работы функций."""
    # Тестовые данные
    transactions = [
        {
            "id": 1,
            "date": "2024-01-15",
            "description": "Перевод другу",
            "amount": 5000,
            "currency": "RUB",
            "status": "EXECUTED"
        },
        {
            "id": 2,
            "date": "2024-01-16",
            "description": "Оплата интернета",
            "amount": 1000,
            "currency": "RUB",
            "status": "EXECUTED"
        },
        {
            "id": 3,
            "date": "2024-01-17",
            "description": "Покупка в магазине",
            "amount": 2500,
            "currency": "RUB",
            "status": "CANCELED"
        },
    ]

    print("Демонстрация работы функций:")
    print("=" * 50)

    # Демонстрация filter_by_status
    print("\n1. Фильтрация по статусу 'EXECUTED':")
    executed = filter_by_status(transactions, "EXECUTED")
    for t in executed:
        print(f"  - {t['description']}: {t['amount']} {t['currency']}")

    # Демонстрация process_bank_search
    print("\n2. Поиск по описанию 'перевод':")
    search_results = process_bank_search(transactions, "перевод")
    for t in search_results:
        print(f"  - {t['description']}")

    # Демонстрация process_bank_operations
    print("\n3. Подсчет операций по категориям:")
    categories = ["Перевод", "Оплата", "Покупка"]
    stats = process_bank_operations(transactions, categories)
    for category, count in stats.items():
        print(f"  - {category}: {count}")

    # Демонстрация validate_status
    print("\n4. Проверка статусов:")
    test_statuses = ["EXECUTED", "executed", "UNKNOWN", "test"]
    for status in test_statuses:
        is_valid = validate_status(status)
        print(f"  - '{status}': {'валиден' if is_valid else 'невалиден'}")


if __name__ == "__main__":
    main()
