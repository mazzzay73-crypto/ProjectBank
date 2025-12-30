from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.bank_search import process_bank_search, process_bank_operations
from src.bank_operations import filter_by_status, validate_status, print_transactions

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


def print_welcome():
    """Выводит приветственное сообщение."""
    print("=" * 60)
    print("Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("=" * 60)


def get_file_type_choice():
    """
    Пользователь выбирает тип файла для загрузки.
    """
    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("0. Выйти из программы")

        choice = input("\nВаш выбор: ").strip()

        if choice == '0':
            print("До свидания!")
            exit(0)
        elif choice == '1':
            print("\nДля обработки выбран JSON-файл.")
            return "JSON"
        elif choice == '2':
            print("\nДля обработки выбран CSV-файл.")
            return "CSV"
        elif choice == '3':
            print("\nДля обработки выбран XLSX-файл.")
            return "XLSX"
        else:
            print("Ошибка: пожалуйста, выберите 1, 2, 3 или 0")


def get_user_status():
    """
    Пользователь вводит статус для фильтрации.
    """
    while True:
        print("\n" + "=" * 60)
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

        status = input("\nСтатус: ").strip()

        # Приводим к единому регистру для проверки
        if validate_status(status):
            print(f"\nОперации отфильтрованы по статусу '{status.upper()}'")
            return status
        else:
            print(f"\nОшибка: статус операции '{status}' недоступен.")
            print("Пожалуйста, введите один из доступных статусов.")


def get_user_search():
    """
    Пользователь вводит строку для поиска в описании.
    """
    print("\n" + "=" * 60)
    print("Введите строку для поиска в описании операций")
    print("(оставьте пустым, чтобы пропустить поиск):")

    search = input("\nПоиск: ").strip()
    return search


def get_user_categories():
    """
    Пользователь вводит категории для анализа.
    """
    print("\n" + "=" * 60)
    print("Хотите получить анализ операций по категориям? (да/нет)")

    while True:
        choice = input("\nВаш выбор: ").strip().lower()

        if choice in ['да', 'д', 'yes', 'y']:
            print("\nВведите категории для анализа через запятую")
            print("Пример: Перевод, Оплата, Покупка")

            categories_input = input("\nКатегории: ").strip()

            if categories_input:
                # Разделяем по запятой и очищаем от пробелов
                categories = [cat.strip() for cat in categories_input.split(',')]
                return categories
            else:
                print("Категории не указаны. Анализ пропущен.")
                return []
        elif choice in ['нет', 'н', 'no', 'n']:
            return []
        else:
            print("Пожалуйста, введите 'да' или 'нет'")


def simulate_file_load(file_type):
    """
    Имитация загрузки данных из файла.
    В реальном приложении здесь была бы загрузка из файла.
    """
    print(f"\nЗагрузка данных из {file_type}-файла...")

    # Вместо реальной загрузки из файла используем тестовые данные
    data = get_sample_data()

    print(f"Успешно загружено {len(data)} транзакций.")
    return data


def main():
    """
    Основная функция программы.
    """
    print_welcome()

    while True:
        # 1. Выбор типа файла
        file_type = get_file_type_choice()

        # 2. Имитация загрузки данных
        data = simulate_file_load(file_type)

        if not data:
            print("\nОшибка: не удалось загрузить данные.")
            continue

        # 3. Пользователь вводит статус для фильтрации
        status = get_user_status()

        # 4. Фильтрация по статусу
        filtered_data = filter_by_status(data, status)

        # 5. Проверка результатов фильтрации
        if not filtered_data:
            print(f"\nНе найдено ни одной транзакции со статусом '{status.upper()}'")

            # Предложить попробовать другой статус
            print("\nХотите попробовать другой статус? (да/нет)")
            retry = input("Ваш выбор: ").strip().lower()

            if retry in ['да', 'д', 'yes', 'y']:
                continue
            else:
                print("\nХотите начать сначала? (да/нет)")
                restart = input("Ваш выбор: ").strip().lower()
                if restart in ['да', 'д', 'yes', 'y']:
                    continue
                else:
                    print("До свидания!")
                    break

        # 6. Пользователь вводит строку для поиска
        search_text = get_user_search()

        if search_text:
            # 7. Поиск по описанию
            search_results = process_bank_search(filtered_data, search_text)

            if not search_results:
                print(f"\nНе найдено транзакций с текстом '{search_text}' в описании")

                # Показать исходные отфильтрованные данные
                print("\nПоказать все транзакции с выбранным статусом? (да/нет)")
                show_all = input("Ваш выбор: ").strip().lower()

                if show_all in ['да', 'д', 'yes', 'y']:
                    final_data = filtered_data
                else:
                    # Предложить новый поиск
                    print("\nХотите ввести другой текст для поиска? (да/нет)")
                    new_search = input("Ваш выбор: ").strip().lower()
                    if new_search in ['да', 'д', 'yes', 'y']:
                        search_text = get_user_search()
                        search_results = process_bank_search(filtered_data, search_text)
                        final_data = search_results if search_results else filtered_data
                    else:
                        continue
            else:
                final_data = search_results
                print(f"\nНайдено {len(final_data)} транзакций с текстом '{search_text}'")
        else:
            final_data = filtered_data

        # 8. Вывод результатов
        print_transactions(final_data)

        # 9. Анализ по категориям (пользователь вводит категории)
        categories = get_user_categories()

        if categories:
            category_stats = process_bank_operations(final_data, categories)

            if category_stats:
                print("\n" + "=" * 60)
                print("Статистика по категориям:")
                print("-" * 40)

                for category, count in category_stats.items():
                    if count > 0:
                        print(f"{category}: {count} операций")
                    else:
                        print(f"{category}: нет операций")
            else:
                print("\nНе удалось получить статистику по категориям.")

        # 10. Повторить или выйти
        print("\n" + "=" * 60)
        print("Хотите выполнить еще один запрос? (да/нет)")

        while True:
            repeat = input("\nВаш выбор: ").strip().lower()

            if repeat in ['да', 'д', 'yes', 'y']:
                break
            elif repeat in ['нет', 'н', 'no', 'n']:
                print("\nДо свидания! Спасибо за использование программы.")
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
