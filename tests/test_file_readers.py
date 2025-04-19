from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.file_readers import csv_reader, excel_reader


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description; "
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 5823391;Счет 397619397;Перевод организации",
)
@patch("src.file_readers.csv.DictReader")
def test_csv_reader(mock_csv: Any, mock_open: Any) -> None:
    """Проверка корректности работы функции c CSV-файлом"""
    csv_reader("fake_path.csv", delimiter=";")
    mock_open.assert_called_once_with("fake_path.csv", encoding="utf-8")
    mock_csv.assert_called_once_with(mock_open(), delimiter=";")


def test_no_csv_data(path_file: str = "any_date.csv") -> Any:
    """Проверка работы функции при отсутствии CSV-файла по заданному пути"""
    assert csv_reader(path_file) == []


@patch("src.file_readers.pd.read_excel", read_data="text")
def test_excel_reader(mock_excel: Any) -> None:
    """Проверка корректности работы функции c Excel-файлом"""
    mock_excel.return_value = pd.DataFrame({"text"})
    assert excel_reader("fake_path.xlsx") == [{0: "text"}]
    mock_excel.assert_called_once_with("fake_path.xlsx")


def test_no_excel_data(path_file: str = "any_date.xlsx") -> Any:
    """Проверка работы функции при отсутствии Excel-файла по заданному пути"""
    assert excel_reader(path_file) == []
