from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Принимает список транзакций и поочередно выдает те, где валюта соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[Any, Any]]) -> Generator:
    """Принимает список словарей с транзакциями, возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for card_number in range(start, stop):
        if 1 <= card_number <= 9999999999999999:
            intermediate_string = (16 - len(str(card_number))) * "0" + str(card_number)
            formatted_string = (
                intermediate_string[0:4]
                + " "
                + intermediate_string[4:8]
                + " "
                + intermediate_string[8:12]

                + " "
                + intermediate_string[-4:]
            )
            yield formatted_string
        else:
            print("Некорректный номер")
