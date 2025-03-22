from typing import Iterator

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]
def filter_by_currency(transactions:list, currency:str) -> Iterator[dict]:
    """Принимает список транзакций и поочередно выдает те, где валюта соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями, возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for card_number in range(start, stop):
        intermediate_string = (16 - len(str(card_number))) * "0" + str(card_number)
        formatted_string = f'{intermediate_string[0:4], intermediate_string[4:8], 
        intermediate_string[8:12], intermediate_string[-4:]}'
        yield formatted_string
