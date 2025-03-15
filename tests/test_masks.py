from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("") == "XXXX XX** **** XXXX"


def test_get_mask_card_number(empty_string):
    assert get_mask_card_number("") == empty_string


def test_get_mask_card_number(not_correct_string):
    assert get_mask_card_number("700079228960636112121") == not_correct_string


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account(empty_string):
    assert get_mask_account("") == empty_string


def test_get_mask_account(not_correct_string):
    assert get_mask_account("4305") == not_correct_string



    