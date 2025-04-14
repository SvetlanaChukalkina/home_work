import re
from collections import Counter

def transactions_search(operation_list, search_string):
    """Принимает список словарей с данными и строку поиска, возвращает список словарей,
    в описании которых есть данная строка"""
    search_result = []
    pattern = re.compile(search_string, flags=re.IGNORECASE)
    for operation in operation_list:
        if "description" in operation:
            if pattern.findall(operation["description"]):
                search_result.append(operation)
    return search_result


def transactions_counter(banking_list, categories):
    """Принимает данные о банковских операциях и список их категорий, возвращает словарь,
    где ключи — названия категорий, а значения — количество операций в них"""
    filtered_banking_list = []
    for operation in banking_list:
        if operation["description"] in categories:
            filtered_banking_list.append(operation["description"])
        counter = Counter(filtered_banking_list)
    return dict(counter)
