from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(currency: str, expected: list[dict]) -> None:
    """Проверка корректности фильтрации транзакций по заданной валюте"""
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    assert (list(filter_by_currency(transactions, currency))) == expected


@pytest.fixture
def data() -> list[dict[Any, Any]]:
    return [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


def test_filter_no_currency(data: list[dict[Any, Any]]) -> None:
    """Проверка обработки случаев, когда транзакции в заданной валюте отсутствуют"""
    result = list(filter_by_currency(data, currency="YEN"))
    assert result == []


@pytest.fixture
def empty_data() -> list[dict[Any, Any]]:
    return []


def test_filter_empty_list(empty_data: list[dict[Any, Any]]) -> None:
    """Проверка работы функции при обработке пустого списка"""
    result = list(filter_by_currency(empty_data, currency="USD"))
    assert result == []


@pytest.fixture
def transactions_data() -> list[dict[Any, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_transaction_descriptions(transactions_data: list[dict[Any, Any]]) -> None:
    """Проверка корректности возврата описания для каждой транзакции"""
    generator = transaction_descriptions(transactions_data)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_empty_transaction_descriptions(empty_data: list[dict[Any, Any]]) -> None:
    """Проверка работы функции при обработке пустого списка"""
    result = list(transaction_descriptions(empty_data))
    assert result == []


def test_card_number_generator() -> None:
    """Проверка корректности работы генератора в заданном диапазоне"""
    generator = card_number_generator(695, 700)
    assert next(generator) == "0000 0000 0000 0695"
    assert next(generator) == "0000 0000 0000 0696"

    generator = card_number_generator(1, 700000000)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"

    generator = card_number_generator(9999999999999998, 10000000000000001)
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"
