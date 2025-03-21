from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Проверка корректности выполнения маскировки"""
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"


def test_get_mask_card_number_empty(empty_string: str) -> None:
    """Проверка корректности отработки в случае ввода пустой строки"""
    assert get_mask_card_number("") == empty_string


def test_get_mask_card_number_not_correct(not_correct_string: str) -> None:
    """Проверка работы функции при вводе некорректного значения"""
    assert get_mask_card_number("70007922896063611") == not_correct_string
    assert get_mask_card_number("700079228960636") == not_correct_string


def test_get_mask_account() -> None:
    """Проверка корректности выполнения маскировки счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_empty(empty_string: str) -> None:
    """Проверка корректности отработки в случае ввода пустой строки"""
    assert get_mask_account("") == empty_string


def test_get_mask_account_not_correct(not_correct_string: str) -> None:
    """Проверка работы функции при вводе некорректного значения"""
    assert get_mask_account("4305") == not_correct_string
