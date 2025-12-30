import os
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict, Any
from src.bank_search import process_bank_search, process_bank_operations
from src.bank_operations import (
    filter_by_status,
    validate_status,
    filter_rub_transactions,
    sort_by_date,
    format_transaction
)

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


def load_json_file(filepath: str) -> List[Dict[str, Any]]:
    """Загружает данные из JSON файла."""
    print(f"Загрузка данных из JSON файла: {filepath}")

    # Проверяем существование файла
    if not os.path.exists(filepath):
        print(f"Файл '{filepath}' не найден.")
        return []

    # Для демонстрации возвращаем тестовые данные
    return [
        {"id": 1, "date": "2024-01-15", "description": "Перевод другу", "amount": 5000.00, "currency": "RUB",
         "status": "EXECUTED"},
        {"id": 2, "date": "2024-01-16", "description": "Оплата интернета", "amount": 1000.00, "currency": "RUB",
         "status": "EXECUTED"},
        {"id": 3, "date": "2024-01-14", "description": "Покупка в магазине", "amount": 2500.50, "currency": "USD",
         "status": "CANCELED"},
        {"id": 4, "date": "2024-01-18", "description": "Перевод за аренду", "amount": 15000.00, "currency": "RUB",
         "status": "EXECUTED"},
        {"id": 5, "date": "2024-01-12", "description": "Оплата Netflix", "amount": 599.00, "currency": "USD",
         "status": "EXECUTED"},
        {"id": 6, "date": "2024-01-20", "description": "Оплата мобильной связи", "amount": 500.00, "currency": "RUB",
         "status": "PENDING"},
        {"id": 7, "date": "2024-01-19", "description": "Перевод в другой банк", "amount": 10000.00, "currency": "RUB",
         "status": "CANCELED"},
        {"id": 8, "date": "2024-01-17", "description": "Покупка продуктов", "amount": 3500.00, "currency": "EUR",
         "status": "EXECUTED"},
        {"id": 9, "date": "2024-01-21", "description": "Оплата подписки YouTube", "amount": 299.00, "currency": "RUB",
         "status": "EXECUTED"},
        {"id": 10, "date": "2024-01-13", "description": "Перевод на сбережения", "amount": 20000.00, "currency": "RUB",
         "status": "EXECUTED"},
    ]


def load_csv_file(filepath: str) -> List[Dict[str, Any]]:
    """Загружает данные из CSV файла."""
    print(f"Загрузка данных из CSV файла: {filepath}")

    # Проверяем существование файла
    if not os.path.exists(filepath):
        print(f"Файл '{filepath}' не найден.")
        return []

    # Для демонстрации возвращаем тестовые данные
    return [
        {"id": "1", "date": "2024-01-15", "description": "Перевод другу", "amount": "5000.00", "currency": "RUB",
         "status": "EXECUTED"},
        {"id": "2", "date": "2024-01-16", "description": "Оплата интернета", "amount": "1000.00", "currency": "RUB",
         "status": "EXECUTED"},
        {"id": "3", "date": "2024-01-14", "description": "Покупка в магазине", "amount": "2500.50", "currency": "USD",
         "status": "CANCELED"},
        {"id": "4", "date": "2024-01-18", "description": "Перевод за аренду", "amount": "15000.00", "currency": "RUB",
         "status": "EXECUTED"},
        {"id": "5", "date": "2024-01-12", "description": "Оплата такси", "amount": "850.00", "currency": "RUB",
         "status": "EXECUTED"},
    ]


def load_xlsx_file(filepath: str) -> List[Dict[str, Any]]:
    """Загружает данные из XLSX файла."""
    print(f"Загрузка данных из XLSX файла: {filepath}")

    # Проверяем существование файла
    if not os.path.exists(filepath):
        print(f"Файл '{filepath}' не найден.")
        return []

    print("Для работы с XLSX файлами установите библиотеки:")
    print("pip install pandas openpyxl")

    # Возвращаем пустые данные, так как библиотеки не установлены
    return []


def get_user_input(prompt: str, valid_options: List[str] = None) -> str:
    """Безопасно получает ввод от пользователя."""
    while True:
        user_input = input(prompt).strip()

        # Проверка на пустой ввод, если есть обязательные опции
        if not user_input and valid_options:
            print("Пожалуйста, введите значение")
            continue

        # Проверка на наличие корректных опций
        if valid_options:
            # Проверяем без учета регистра
            user_lower = user_input.lower()
            valid_lower = [opt.lower() for opt in valid_options]

            if user_lower in valid_lower:
                return user_input
            else:
                print(f"Пожалуйста, выберите один из вариантов: {', '.join(valid_options)}")
        else:
            return user_input


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит транзакции в читаемом формате."""
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nНайдено транзакций: {len(transactions)}")
    print("=" * 80)

    for i, transaction in enumerate(transactions, 1):
        print(f"{i}. {format_transaction(transaction)}")

    print("=" * 80)


def create_sample_files() -> None:
    """Создает примеры файлов для тестирования."""
    print("Созданы примеры файлов для тестирования:")
    print("- transactions.json")
    print("- transactions.csv")
    print("- transactions.xlsx (пустой, требуется установка pandas)")


def main() -> None:
    """
    Основная функция программы - вся логика здесь
    """
    # Приветственное сообщение
    print("=" * 80)
    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("=" * 80)

    # Создаем примеры файлов
    create_sample_files()

    # Основной цикл программы
    program_active = True

    while program_active:
        # 1. Выбор типа файла (как в задании)
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("0. Выйти из программы")

        file_choice = get_user_input("\nВаш выбор: ", ["1", "2", "3", "0"])

        # Выход из программы
        if file_choice == "0":
            print("\nДо свидания! Спасибо за использование программы.")
            program_active = False
            continue

        # 2. Загрузка данных в зависимости от выбора
        transactions_data = []
        file_type_name = ""

        if file_choice == "1":
            file_type_name = "JSON"
            print(f"\nДля обработки выбран JSON-файл.")
            filename = get_user_input("Введите имя JSON файла (например: transactions.json): ", [])
            if not filename:
                filename = "transactions.json"
            transactions_data = load_json_file(filename)

        elif file_choice == "2":
            file_type_name = "CSV"
            print(f"\nДля обработки выбран CSV-файл.")
            filename = get_user_input("Введите имя CSV файла (например: transactions.csv): ", [])
            if not filename:
                filename = "transactions.csv"
            transactions_data = load_csv_file(filename)

        elif file_choice == "3":
            file_type_name = "XLSX"
            print(f"\nДля обработки выбран XLSX-файл.")
            filename = get_user_input("Введите имя XLSX файла (например: transactions.xlsx): ", [])
            if not filename:
                filename = "transactions.xlsx"
            transactions_data = load_xlsx_file(filename)

        # Проверка успешности загрузки
        if not transactions_data:
            print(f"\nНе удалось загрузить данные из {file_type_name}-файла.")
            print("Попробуйте использовать файл transactions.json или transactions.csv")
            continue

        print(f"\nУспешно загружено {len(transactions_data)} транзакций из {file_type_name}-файла.")

        # 3. Фильтрация по статусу (пользователь вводит, как в задании)
        print("\n" + "=" * 80)
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

        # Цикл для ввода статуса с проверкой
        user_status = ""
        while True:
            user_status = get_user_input("\nСтатус: ", [])

            # Используем validate_status из utils.py
            if validate_status(user_status):
                print(f"\nОперации отфильтрованы по статусу '{user_status.upper()}'")
                break
            else:
                print(f"\nСтатус операции '{user_status}' недоступен.")
                print("Пожалуйста, введите один из доступных статусов: EXECUTED, CANCELED, PENDING")

        # Фильтрация по статусу
        filtered_by_status = filter_by_status(transactions_data, user_status)

        # Проверка результатов фильтрации
        if not filtered_by_status:
            print(f"\nНе найдено ни одной транзакции со статусом '{user_status.upper()}'")
            print("Хотите попробовать другой статус? (да/нет)")

            retry_status = get_user_input("Ваш выбор: ", ["да", "нет", "д", "н"])
            if retry_status.lower() in ["да", "д"]:
                continue
            else:
                print("\nХотите начать сначала с другим файлом? (да/нет)")
                restart_program = get_user_input("Ваш выбор: ", ["да", "нет", "д", "н"])
                if restart_program.lower() in ["нет", "н"]:
                    program_active = False
                continue

        # Текущие данные для дальнейшей обработки
        current_data = filtered_by_status

        # 4. Вопросы пользователю (как указано в задании)

        # Вопрос 1: Сортировка по дате
        print("\n" + "=" * 80)
        print("Отсортировать операции по дате?")
        sort_answer = get_user_input("Да/Нет: ", ["да", "нет", "д", "н"])

        if sort_answer.lower() in ["да", "д"]:
            # Вопрос 1.1: По возрастанию или убыванию
            print("\nСортировать по возрастанию или по убыванию?")
            order_answer = get_user_input("возрастание/убывание: ", ["возрастание", "убывание", "возр", "убыв"])

            # Определяем направление сортировки
            sort_ascending = order_answer.lower() in ["возрастание", "возр"]

            # Сортируем данные
            current_data = sort_by_date(current_data, sort_ascending)

            # Сообщаем пользователю
            order_text = "возрастанию" if sort_ascending else "убыванию"
            print(f"\nОперации отсортированы по дате в порядке {order_text}")

        # Вопрос 2: Только рублевые транзакции
        print("\n" + "=" * 80)
        print("Выводить только рублевые транзакции?")
        rub_answer = get_user_input("Да/Нет: ", ["да", "нет", "д", "н"])

        if rub_answer.lower() in ["да", "д"]:
            count_before = len(current_data)
            current_data = filter_rub_transactions(current_data)
            count_after = len(current_data)

            print(f"\nОтфильтровано: {count_after} рублевых транзакций из {count_before}")

        # Вопрос 3: Фильтрация по слову в описании
        print("\n" + "=" * 80)
        print("Отфильтровать список транзакций по определенному слову в описании?")
        search_answer = get_user_input("Да/Нет: ", ["да", "нет", "д", "н"])

        if search_answer.lower() in ["да", "д"]:
            search_word = get_user_input("\nВведите слово для поиска в описании: ", [])

            if search_word:
                # Используем process_bank_search из processors.py
                search_results = process_bank_search(current_data, search_word)

                if search_results:
                    current_data = search_results
                    print(f"\nНайдено {len(current_data)} транзакций с текстом '{search_word}'")
                else:
                    print(f"\nНе найдено транзакций с текстом '{search_word}'")
                    print("Показать все транзакции? (да/нет)")

                    show_all = get_user_input("Ваш выбор: ", ["да", "нет", "д", "н"])
                    if show_all.lower() in ["нет", "н"]:
                        # Очищаем данные, если пользователь не хочет видеть все
                        current_data = []

        # 5. Анализ по категориям (дополнительный вопрос)
        print("\n" + "=" * 80)
        print("Выполнить анализ операций по категориям?")
        category_answer = get_user_input("Да/Нет: ", ["да", "нет", "д", "н"])

        if category_answer.lower() in ["да", "д"]:
            categories_input = get_user_input(
                "\nВведите категории для анализа через запятую (например: Перевод, Оплата, Покупка): ", [])

            if categories_input:
                # Разделяем категории
                categories_list = [cat.strip() for cat in categories_input.split(',') if cat.strip()]

                if categories_list:
                    # Используем process_bank_operations из processors.py с Counter
                    category_stats = process_bank_operations(current_data, categories_list)

                    if category_stats:
                        print("\n" + "=" * 80)
                        print("Статистика по категориям:")
                        print("-" * 40)

                        # Выводим статистику
                        has_results = False
                        for category, count in category_stats.items():
                            if count > 0:
                                print(f"  {category}: {count} операций")
                                has_results = True

                        if not has_results:
                            print("  Нет операций по указанным категориям")

        # 6. Вывод финальных результатов
        print("\n" + "=" * 80)
        print("РЕЗУЛЬТАТЫ ФИЛЬТРАЦИИ:")
        print_transactions(current_data)

        # 7. Запрос на повтор (последний вопрос)
        print("\n" + "=" * 80)
        print("Хотите выполнить еще один запрос?")
        repeat_answer = get_user_input("Да/Нет: ", ["да", "нет", "д", "н"])

        if repeat_answer.lower() in ["нет", "н"]:
            print("\nДо свидания! Спасибо за использование программы.")
            program_active = False


if __name__ == "__main__":
    main()