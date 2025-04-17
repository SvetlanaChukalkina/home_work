import pytest


@pytest.fixture
def empty_string() -> str:
    """Проверка случаев с вводом пустой строки"""
    return "Данные не введены"


@pytest.fixture
def not_correct_string() -> str:
    """Проверка случаев с некорректным вводом строки"""
    return "Данные введены неверно"


# @pytest.fixture
# def missing_filter() -> str:
#   """Проверка случаев с некорректным вводом значения фильтра"""
#  return "Выбранное значение отсутствует"
