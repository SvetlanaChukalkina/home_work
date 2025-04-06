from unittest.mock import patch
from typing import Any
import pytest

from src.external_api import transaction_conversation


@pytest.fixture
def test_transaction_data() -> list[dict]:
    """Проверка работы функции с корректными входными данными"""
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]


def test_transaction_conversation(test_transaction_data: list[dict]) -> Any:
    assert transaction_conversation(test_transaction_data) == [43318.34]


@pytest.fixture
def test_transaction_no_data() -> list[dict]:
    """Проверка работы функции при отсутствии заданного значения"""
    return [{"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404"}]


def test_transaction_no_conversation(test_transaction_no_data: list[dict]) -> None:
    assert transaction_conversation(test_transaction_no_data) == ["Нет доступного значения"]


@patch("src.external_api.requests.get")
def test_api_transaction_conversation(mock_request: Any) -> Any:
    """Проверка работы функции при необходимости обращения к внешнему API"""
    test_data = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "318.34", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]

    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = [6677989.02481, 29448.907585]

    result = transaction_conversation(test_data)
    assert result == [6677989.02481, 29448.907585]
