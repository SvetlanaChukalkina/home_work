from src.utils import get_transactions_info
from src.file_readers import csv_reader, excel_reader
import re
from src.operations import transactions_search
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.masks import get_mask_card_number, get_mask_account

def main():
    user_input_file = input("""
    Привет!
    Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)
    if user_input_file not in ["1", "2", "3"]:
        print("Тип файла не выбран или введены некорректные данные.")
    else:
        input_variants = {"1": "JSON", "2": "CSV", "3": "XLSX"}
        user_choise = input_variants.get(user_input_file)
        print(f"Для обработки выбран {user_choise}-файл.")

        while True:
            user_input_status = input("""
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
             """)
            if user_input_status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f'Статус операции \"{user_input_status}\" недоступен.')
            else:
                print(f'Операции отфильтрованы по статусу {user_input_status.upper()}')
                break
        user_input_sort = input("""Отсортировать операции по дате? Да/Нет
        """).lower()
        if user_input_sort == "да":
            user_input_range = input("""Отсортировать по возрастанию или по убыванию?
            По возрастанию / по убыванию
            """).lower()
        user_input_currency = input("""Выводить только рублевые тразакции? Да/Нет
        """).lower()

        user_input_description = input("""Отфильтровать список транзакций
        по определенному слову в описании? Да/Нет
        """).lower()

        # Выбор формата исходного файла
        if user_choise == "JSON":
            initial_data = get_transactions_info(path="data/operations.json")
        elif user_choise == "CSV":
            initial_data = csv_reader(path="data/transactions.csv")
        else:
            initial_data = excel_reader(path="data/transactions_excel.xlsx")


        #Фильтрация операций по выбранному слову в описании
        filtered_transaction = filter_by_state(list_of_values=initial_data, state=user_input_status)

        #Сортировка по дате
        if user_input_sort == "да" and user_input_range == "по убыванию":
            sorted_filtered_transaction = sort_by_date(list_of_values=filtered_transaction)
        elif user_input_sort == "да" and user_input_range == "по возрастанию":
            sorted_filtered_transaction = sort_by_date(list_of_values=filtered_transaction, reverse = False)
        else:
            sorted_filtered_transaction = filtered_transaction

        #Выбор валюты операций
        if user_input_currency == "да": #and "RUB" in sorted_filtered_transaction:
            update_list = []
            search_string = "RUB"
            pattern = re.compile(search_string)
            for i in sorted_filtered_transaction:
                if pattern.findall(i['operationAmount']['currency']['code']):
                    update_list.append(i)
        else:
            update_list = sorted_filtered_transaction
        # for up in update_list:
        #     print(up)

        #Поиск по ключевым словам в описании транзакции
        if user_input_description == "нет":
            final_list = update_list
        elif user_input_description == "да":
            word_input = input("""Введите ключевое слово для поиска
            """)
            final_list = transactions_search(operation_list=update_list, search_string=word_input)


        #Вывод результатов
        print("Распечатываю итоговый список транзакций...")

        for fi in final_list:
            unformatted_date = fi["date"]
            formatted_date = get_date(unformatted_date)
            operation_sum = fi['operationAmount']['amount'] + fi['operationAmount']['currency']['name']
            operation_name = fi["description"]
            receiver = fi['to']
            if "Счет" in receiver:
                mask_receiver = get_mask_account(receiver)
            elif "Счет" not in receiver:
                mask_receiver = mask_account_card(receiver)
            sender = fi['to']
            if "Счет" in sender:
                mask_sender = get_mask_account(sender)
            elif "Счет" not in sender:
                mask_sender = mask_account_card(sender)

            if operation_name != "Открытие вклада":


                print(f"""{formatted_date}  {operation_name},
                {mask_sender} -> {mask_receiver},
                Сумма: {operation_sum}""")
            else:
                print(f"""{formatted_date} {operation_name},{mask_receiver},
                Сумма: {operation_sum}""")



#     print(f"""Всего банковских операций в выборке:

    # 08.12.2019 Открытие вклада 
    # Счет **4321
    # Сумма: 40542 руб. 
    # 
    # 12.11.2019 Перевод с карты на карту
    # MasterCard 7771 27  3727 -> Visa Platinum 1293 38 **** 9203
    # Сумма: 130 USD
    #

main()
