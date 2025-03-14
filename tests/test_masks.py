from src.masks import get_mask_card_number, get_mask_account

def test_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    assert get_mask_card_number("700079228960636112121") == "Номер карты введен неверно"

    assert get_mask_card_number("") == "Введите номер карты"


def test_account():
    assert get_mask_account("73654108430135874305") == "**4305"

    assert get_mask_account("874305") == "**4305"

    assert get_mask_account("") == "Введите номер счета"

    assert get_mask_account("4305") == "Номер счета введен неверно"