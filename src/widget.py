from src.masks import get_mask_account, get_mask_card_number
"""Импортируем функции для скрытия номера карты и счета из masks"""
def mask_account_card(card_info: str) -> str:
    """Функция принимает строку и выводит замаскированный номер"""
    number = ""
    type_of_inf = ""

    for part in card_info:
        if part.isdigit():
            number += part
        elif part.isalpha():
            type_of_inf += part

    if type_of_inf == "счет" or type_of_inf == "Счет":
        masked_result = get_mask_account(number)
    else:
        masked_result = get_mask_card_number(number)

    return f"{type_of_inf} [{masked_result}]"

card_info = input("Please enter your number: ")
result = mask_account_card(card_info)
print(result)