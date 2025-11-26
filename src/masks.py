def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты card_number, удаляет пробелы и возвращает замаскированный номер с пробелами"""

    cleaned_number = card_number.replace(" ", "")
    if len(cleaned_number) > 0:
        return f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4:]}"
    return ""


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета account_number и возвращает замаскированный номер"""

    if len(account_number) > 0:
        return f"**{account_number[-4:]}"
    return ""
