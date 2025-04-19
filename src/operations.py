import re
from collections import Counter
from typing import Any


def transactions_search(operation_list: list[dict], search_string: str) -> list[dict[Any, Any]] | str:
    """Принимает список словарей с данными и строку поиска, возвращает список словарей,
    в описании которых есть данная строка"""
    search_result = []
    pattern = re.compile(search_string, flags=re.IGNORECASE)
    for operation in operation_list:
        if "description" in operation:
            if pattern.findall(operation["description"]):
                search_result.append(operation)
    if len(search_result) == 0:
        return "Указанная строка не найдена"
    return search_result


def transactions_counter(banking_list: list[dict], categories: list) -> dict[Any, Any] | str:
    """Принимает данные о банковских операциях и список их категорий, возвращает словарь,
    где ключи — названия категорий, а значения — количество операций в них"""
    if len(categories) == 0:
        return "Категории не выбраны"
    else:
        filtered_banking_list = []
        for operation in banking_list:
            if "description" in operation and operation["description"] in categories:
                filtered_banking_list.append(operation["description"])
        counter = Counter(filtered_banking_list)
        for category in categories:
            if category not in counter.keys():
                zero_counter = {category: 0}
                counter.update(zero_counter)
    return dict(counter)
