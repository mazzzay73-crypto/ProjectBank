def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты card_number, удаляет пробелы и возвращает замаскированный номер с пробелами"""
    print()

    return f"{card_number[:4]} {card_number[5:7]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета account_number и возвращает замаскированный номер"""

    return f"**{account_number[-4:]}"
