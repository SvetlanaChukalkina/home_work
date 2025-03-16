import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_types_of_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_mask_account_empty(empty_string: str) -> None:
    assert mask_account_card("") == empty_string


def test_mask_account_not_correct_card(not_correct_string: str) -> None:
    assert mask_account_card("Счет 5678") == not_correct_string
    assert mask_account_card("Visa Gold 15545678") == not_correct_string
    assert mask_account_card("Visa Platinum 15557674757674576456") == not_correct_string


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-12-071T02:26:18.671407", "07.12.2022"),
        ("2021-05-201T02:26:18.671407", "20.05.2021"),
        ("2022-08-311T02:26:18.671407", "31.08.2022"),
        ("2022-06-301T02:26:18.671407", "30.06.2022"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected


def test_get_not_correct_date(not_correct_string: str) -> None:
    assert get_date("2024-15-11T02:26:18.671407") == not_correct_string
    assert get_date("2024-10-41T02:26:18.671407") == not_correct_string
    assert get_date("2A24-10-41T02:26:18.671407") == not_correct_string
    assert get_date("2024-1T-41T02:26:18.671407") == not_correct_string
    assert get_date("2024-10-N1T02:26:18.671407") == not_correct_string


def test_get_empty_date(empty_string: str) -> None:
    assert get_date("") == empty_string
