import json
import logging
from typing import Any

utils_logger = logging.getLogger()
utils_file_handler = logging.FileHandler("../logs/utils.log", "w")
utils_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_transactions_info(path: str) -> list[dict[Any, Any]]:
    """Принимает путь до JSON-файла, возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                transaction_list = list(json.load(json_file))
                utils_logger.info("Data is load")
                return transaction_list
            except json.JSONDecodeError:
                utils_logger.error("Incorrect format")
                return []
    except FileNotFoundError:
        utils_logger.error("File not found")
        return []
