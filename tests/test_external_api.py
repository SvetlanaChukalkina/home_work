from typing import Any
from unittest.mock import patch

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
        },
        {
            "id": 357684376,
            "state": "EXECUTED",
            "date": "2017-10-15T08:15:40.190024",
            "operationAmount": {"amount": "15.0", "currency": {"name": "руб.", "code": "RUB"}},
        },
    ]


def test_transaction_conversation(test_transaction_data: list[dict]) -> Any:
    assert transaction_conversation(test_transaction_data) == [43318.34, 15.0]


@pytest.fixture
def test_transaction_no_data() -> list[dict]:
    """Проверка работы функции при отсутствии заданного значения"""
    return [{"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404"}]


def test_transaction_no_conversation(test_transaction_no_data: list[dict]) -> Any:
    assert transaction_conversation(test_transaction_no_data) == [0.00]


@patch("src.external_api.conversation")
def test_transaction_conversation_without_requests(convers_mock: Any) -> None:
    """Проверка работы функции без необходимости обращения к внешнему API"""
    test_data = [
        {"operationAmount": {"amount": 15.57, "currency": {"code": "RUB"}}},
        {"no_needed_key": "ok"},
        {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": 200, "currency": {"code": "EUR"}}},
    ]
    convers_mock.side_effect = [2.05, 7.97]
    result = transaction_conversation(test_data)

    assert result == [15.57, 0.0, 2.05, 7.97]
    assert convers_mock.call_count == 2
