from datetime import datetime
from typing import Any


def filter_by_state(list_of_values: list[dict[Any, Any]], state: str = "EXECUTED") -> list[dict[Any, Any]]:
    """Возвращает список словарей, у которых ключ state соответствует указанному значению"""
    filter_list = []
    for value in list_of_values:
        if "state" in value and value["state"] == state:
            filter_list.append(value)
    return filter_list


def sort_by_date(list_of_values: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает список, отсортированный по дате"""
    return sorted(list_of_values, key=lambda x: datetime.strptime(x["date"][0:10], "%Y-%m-%d"), reverse=reverse)
