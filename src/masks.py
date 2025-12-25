from .log_config import setup_logger

logger = setup_logger('masks')


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты card_number, удаляет пробелы
    и возвращает замаскированный номер с пробелами"""

    logger.info(f"get_mask_card_number: {card_number}")

    cleaned_number = card_number.replace(" ", "")
    if len(cleaned_number) > 0:
        result = f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4:]}"
        logger.info(f"Card masked: {card_number} -> {result}")
        return result

    logger.warning("Empty string for card")
    return ""


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета account_number
     и возвращает замаскированный номер"""

    logger.info(f"get_mask_account: {account_number}")

    if len(account_number) > 0:
        result = f"**{account_number[-4:]}"
        logger.info(f"Account masked: {account_number} -> {result}")
        return result

    logger.warning("Empty string for account")
    return ""