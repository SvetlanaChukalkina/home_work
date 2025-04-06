import json
from typing import Any


def get_transactions_info(path: str) -> list[dict[Any, Any]]:
    """Принимает путь до JSON-файла, возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                transaction_list = list(json.load(json_file))
                return transaction_list
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
