import json
from unittest.mock import mock_open, patch
from typing import Any

import pytest

from src.utils import get_transactions_info


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",'
    '"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]',
)
@patch("src.utils.json.load")
def test_get_transactions_info(mock_json_load: Any, mock_open: Any) -> None:
    """Проверка корректности работы функции c JSON-файлом"""
    get_transactions_info("fake_path.json")
    mock_open.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once_with(mock_open())


@pytest.fixture
def empty_read_data() -> str:
    """Проверка выполнения функции при передаче некорректного аргумента"""
    return "hjkdsfghsjk"


def test_get_empty_transactions_info(empty_read_data: str) -> None:
    assert get_transactions_info(empty_read_data) == []


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
@patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: Any, mock_open: Any) -> None:
    """Проверка работы функции при ошибке json.JSONDecodeError"""
    result = get_transactions_info("fake_path.json")
    assert result == []
    mock_open.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once()
