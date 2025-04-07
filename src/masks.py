import logging
from typing import Union

masks_logger = logging.getLogger()
masks_file_handler = logging.FileHandler("../logs/masks.log", "w")
masks_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)
masks_logger.addHandler(masks_file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает номер карты в виде числа и возвращает маску XXXX XX** **** XXXX"""
    if len(card_number) == 16:
        masks_logger.info("Card number is correct")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 0:
        masks_logger.error("No data")
        return "Данные не введены"
    masks_logger.error("Not correct data")
    return "Данные введены неверно"


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску **XXXX"""
    if len(account_number) >= 6:
        masks_logger.info("Account number is correct")
        return f"**{account_number[-4:]}"
    elif len(account_number) == 0:
        masks_logger.error("No data")
        return "Данные не введены"
    masks_logger.error("Not correct data")
    return "Данные введены неверно"
