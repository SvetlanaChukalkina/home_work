from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает номер карты в виде числа и возвращает маску XXXX XX** **** XXXX"""
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 0:
        return("Данные не введены")
    return("Данные введены неверно")


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску **XXXX"""
    if len(account_number) >= 6:
        return f"**{account_number[-4:]}"
    elif len(account_number) == 0:
        return("Данные не введены")
    return ("Данные введены неверно")
