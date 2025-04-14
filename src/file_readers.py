import csv
from typing import Any

import pandas as pd


def csv_reader(path: str, delimiter: str = ";") -> list[dict[Any, Any]]:
    """Cчитывает данные из CSV-файла, возвращает список словарей с транзакциями"""
    try:
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []


def excel_reader(path: str) -> list[dict]:
    """Cчитывает данные из Excel-файла, возвращает список словарей с транзакциями"""
    try:
        excel_data = pd.read_excel(path)
        excel_data_list = excel_data.to_dict(orient="records")
        return excel_data_list
    except FileNotFoundError:
        return []
