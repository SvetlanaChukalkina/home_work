from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает номер карты в виде числа и возвращает маску XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску **XXXX"""
    return f"**{account_number[-4:]}"


print(get_mask_card_number("54690309983489"))
print(get_mask_account("54690357876545678"))
