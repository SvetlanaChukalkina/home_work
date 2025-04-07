import json
import logging
from typing import Any

logger = logging.getLogger()
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_info(path: str) -> list[dict[Any, Any]]:
    """Принимает путь до JSON-файла, возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                transaction_list = list(json.load(json_file))
                logger.info("Data is load")
                return transaction_list
            except json.JSONDecodeError:
                logger.error("Incorrect format")
                return []
    except FileNotFoundError:
        logger.error("File not found")
        return []
