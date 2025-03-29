import pytest
from src.decorators import log

def test_log():
    @log(filename="logs.txt")
    def my_function(x, y):
        return x + y
    assert(my_function(1, 2)) == 3


def test_log_error():
    @log
    def my_function(x, y):
        return x / y
        with pytest.raises(ZeroDivisionError):
            my_function(2, 0)

