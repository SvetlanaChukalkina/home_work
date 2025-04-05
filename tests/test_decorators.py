from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> Any:
    """Проверка вывода при корректной отработке функции"""

    @log(filename=None)
    def my_function(x: int | float, y: int | float) -> int | float:
        return x + y

    my_function(10, 20)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error(capsys: Any) -> None:
    """Проверка вывода при выбрасывании ошибки division by zero"""

    @log(filename=None)
    def my_function(x: int | float, y: int | float) -> int | float:
        return x / y

    my_function(10, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (10, 0), {}\n"
