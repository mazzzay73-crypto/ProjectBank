from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_info: str) -> str:
    parts = card_info.split()
    number = parts[-1]
    type_of_inf = parts[0]

    if type_of_inf == "счет" or type_of_inf == "Счет":
        masked_result = get_mask_account(number)
    else:
        masked_result = get_mask_card_number(number)

    return f"{parts[0]} [**{masked_result}**]"