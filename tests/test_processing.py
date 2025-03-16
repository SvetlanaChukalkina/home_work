import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(state, expected):
    """Фильтрация списка словарей по заданному статусу state"""
    list_of_values = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(list_of_values, state) == expected


def test_filter_by_missing_state(missing_filter):
    """Проверка работы при отсутствии словарей с указанным статусом state"""
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            state="DELETED",
        )
        == missing_filter
    )


@pytest.mark.parametrize(
    "date, expected",
    [
        (
            [{"date": "2019-07-03"}, {"date": "2018-06-30"}, {"date": "2018-09-12"}],
            [{"date": "2019-07-03"}, {"date": "2018-09-12"}, {"date": "2018-06-30"}],
        ),
        (
            [{"date": "2019-07-03"}, {"date": "2018-06-30"}, {"date": "2019-07-03"}],
            [{"date": "2019-07-03"}, {"date": "2019-07-03"}, {"date": "2018-06-30"}],
        ),
        ([{"date": "2018-09-12"}, {"date": "2018-10-14"}], [{"date": "2018-10-14"}, {"date": "2018-09-12"}]),
    ],
)
def test_sort_by_date(date, expected):
    """Тестирование сортировки списка словарей по датам в порядке убывания"""
    assert sort_by_date(date) == expected


def test_reverse_sort_by_date()-> None:
    """Тестирование сортировки списка словарей по датам в порядке возрастания"""
    assert (sort_by_date([{"date": "2019-07-03"}, {"date": "2018-06-30"}], reverse=False)) == [
        {"date": "2018-06-30"},
        {"date": "2019-07-03"},
    ]


@pytest.fixture
def not_correct_date():
    """Проверка работы функции с некорректными форматами дат"""
    return [{"date": "12-03-18"}]


def test_correct_date(not_correct_date):
    """Проверка работы функции с некорректными форматами дат"""
    with pytest.raises(ValueError):
        sort_by_date(not_correct_date)
