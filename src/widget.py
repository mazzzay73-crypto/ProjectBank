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

def get_date(date: str) -> str:

    year_month_day = ""
    year = ""
    month = ""
    day = ""

    split_date = date.split("T")
    year_month_day = split_date[0]
    year = year_month_day[0:4]
    month = year_month_day[5:7]
    day = year_month_day[8:]

    return f"{day}.{month}.{year}"

date = input("Please enter date")
correct_day = get_date(date)
print (correct_day)

card_info = input("Please enter your number: ")
result = mask_account_card(card_info)
print(result)