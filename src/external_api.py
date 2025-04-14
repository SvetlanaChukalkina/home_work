import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def conversation(currency: str, amount: str) -> Any:
    """Обращается к внешнему API для получения курса валют и конвертации суммы в рубли"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": API_KEY}
    response = requests.request("GET", url, headers=headers, params=payload)

    status_code = response.status_code
    if status_code == 200:
        return response.json()["result"]
    else:
        print(f"Ошибка запроса: {response.reason}")


def transaction_conversation(transaction_data_list: list[dict[Any, Any]]) -> list:
    """Принимает на вход транзакцию и возвращает ее сумму в рублях"""
    sum_list = []
    for transaction in transaction_data_list:
        if "operationAmount" in transaction:
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["code"]
            if currency == "EUR" or currency == "USD":
                transaction_sum = conversation(
                    amount=transaction["operationAmount"]["amount"],
                    currency=transaction["operationAmount"]["currency"]["code"],
                )
                sum_list.append(float(transaction_sum))
            elif currency == "RUB":
                sum_list.append(float(amount))
        else:
            sum_list.append(0.00)
    return sum_list
