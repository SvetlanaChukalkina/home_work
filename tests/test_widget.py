import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
   assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
   assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize("value, expected",
                         [("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 73654108430135874305", "Счет **4305"),])
def test_mask_account_types_of_card(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_empty(empty_string):
    assert mask_account_card("") == empty_string

def test_mask_account_not_correct_card(not_correct_string):
    assert mask_account_card("Счет 5678") == not_correct_string
    assert mask_account_card("Visa Gold 15545678") == not_correct_string
    assert mask_account_card("Visa Platinum 15557674757674576456") == not_correct_string


#def test_get_mask_card_number(empty_string):
   # assert get_mask_card_number("") == empty_string


#def test_get_mask_card_number(not_correct_string):
  #  assert get_mask_card_number("700079228960636112121") == not_correct_string


#def test_get_date():
   # assert get_mask_account("73654108430135874305") == "**4305"