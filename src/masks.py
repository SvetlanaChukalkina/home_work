import logging
from typing import Union

logger = logging.getLogger()
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает номер карты в виде числа и возвращает маску XXXX XX** **** XXXX"""
    if len(card_number) == 16:
        logger.info("Card number is correct")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 0:
        logger.error("No data")
        return "Данные не введены"
    logger.error("Not correct data")
    return "Данные введены неверно"


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску **XXXX"""
    if len(account_number) >= 6:
        logger.info("Account number is correct")
        return f"**{account_number[-4:]}"
    elif len(account_number) == 0:
        logger.error("No data")
        return "Данные не введены"
    logger.error("Not correct data")
    return "Данные введены неверно"
