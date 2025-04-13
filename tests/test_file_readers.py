from src.file_readers import csv_reader, excel_reader
from unittest.mock import mock_open, patch
from typing import Any

@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='id;state;date;amount;currency_name;currency_code;from;to;description; '
              '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации'    )
@patch("src.file_readers.csv.DictReader")
def test_csv_reader(mock_json_load: Any, mock_open: Any) -> None:
    """Проверка корректности работы функции c CSV-файлом"""
    csv_reader("fake_path.csv")
    mock_open.assert_called_once_with("fake_path.csv", "r", encoding="utf-8")
    mock_json_load.assert_called_once_with(mock_open())