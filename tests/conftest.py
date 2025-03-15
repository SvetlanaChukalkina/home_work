import pytest


@pytest.fixture
def empty_string():
    return "Данные не введены"

@pytest.fixture
def not_correct_string():
    return "Данные введены неверно"

