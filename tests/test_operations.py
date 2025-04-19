from typing import Any

import pytest

from src.operations import transactions_counter, transactions_search


@pytest.fixture
def operations_data() -> list[dict]:
    return [
        {"id": 12341234, "date": "2019-02-04T23:20:00.206878", "description": "Перевод со счета на счет"},
        {"id": 23452345, "date": "2019-03-04T23:20:01.206878", "description": "Перевод со счета на счет"},
        {"id": 34563456, "date": "2019-04-04T23:20:02.206878"},
        {"id": 45674567, "date": "2019-05-04T23:20:03.206878", "description": "Перевод организации"},
    ]


def test_transactions_search(operations_data: list[dict[Any, Any]]) -> None:
    """Проверка корректности работы функции с заданным значением для поиска"""
    # test_operation_list = list(operations_data())
    assert transactions_search(operations_data, search_string="Перевод") == [
        {"id": 12341234, "date": "2019-02-04T23:20:00.206878", "description": "Перевод со счета на счет"},
        {"id": 23452345, "date": "2019-03-04T23:20:01.206878", "description": "Перевод со счета на счет"},
        {"id": 45674567, "date": "2019-05-04T23:20:03.206878", "description": "Перевод организации"},
    ]

    assert transactions_search(operations_data, search_string="Перевод организации") == [
        {"id": 45674567, "date": "2019-05-04T23:20:03.206878", "description": "Перевод организации"}
    ]

    assert (
        transactions_search(operations_data, search_string="Перевод между своими счетами")
        == "Указанная строка не найдена"
    )


def test_transactions_counter(operations_data: list[dict]) -> None:
    """Проверка корректности работы функции с различными вариантами списков категорий"""
    assert transactions_counter(operations_data, categories=[]) == "Категории не выбраны"
    assert transactions_counter(operations_data, categories=["Перевод со счета на счет", "Перевод организации"]) == {
        "Перевод со счета на счет": 2,
        "Перевод организации": 1,
    }
    assert transactions_counter(
        operations_data, categories=["Перевод со счета на счет", "Перевод организации", "Перевод между своими счетами"]
    ) == {"Перевод со счета на счет": 2, "Перевод организации": 1, "Перевод между своими счетами": 0}
    assert transactions_counter(operations_data, categories=["Перевод со счета на счет", "Зачисление зарплаты"]) == {
        "Перевод со счета на счет": 2,
        "Зачисление зарплаты": 0,
    }
