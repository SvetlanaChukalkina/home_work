from src.utils import get_transactions_info
from src.file_readers import csv_reader, excel_reader
import re
from src.operations import transactions_search
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.masks import get_mask_account

def main():
    while True:
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
            break

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

    while True:
        user_input_sort = input("""Отсортировать операции по дате? Да/Нет
        """).lower()
        if user_input_sort not in ["да", "нет"]:
            print("Выберите одно из предложенных значений.")
        elif user_input_sort == "да":
            while True:
                user_input_range = input("""Отсортировать по возрастанию или по убыванию?
                По возрастанию / по убыванию
                """).lower()
                if user_input_range not in ["по возрастанию", "по убыванию"]:
                    print("Выберите одно из предложенных значений.")
                else:
                    break
            break
        else:
            break

    while True:
        user_input_currency = input("""Выводить только рублевые тразакции? Да/Нет
        """).lower()
        if user_input_currency not in ["да", "нет"]:
            print("Выберите одно из предложенных значений.")
        else:
            break

    while True:
        user_input_description = input("""Отфильтровать список транзакций
        по определенному слову в описании? Да/Нет
        """).lower()
        if user_input_description in ["да", "нет"]:
            break
        else:
            print("Выберите одно из предложенных значений.")

    # Выбор формата исходного файла
    if user_choise == "JSON":
        initial_data = get_transactions_info(path="data/operations.json")
    elif user_choise == "CSV":
        initial_data = csv_reader(path="data/transactions.csv")
    else:
        initial_data = excel_reader(path="data/transactions_excel.xlsx")

    # print(initial_data)


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
    if user_input_currency == "да":
        update_list = []
        search_string = "RUB"
        pattern = re.compile(search_string)
        if user_choise == "JSON":
            for i in sorted_filtered_transaction:
                if pattern.findall(i['operationAmount']['currency']['code']):
                    update_list.append(i)
        elif user_choise == "CSV" or user_choise == "XLSX":
            for i in sorted_filtered_transaction:
                if pattern.findall(i['currency_code']):
                    update_list.append(i)
    else:
        update_list = sorted_filtered_transaction

    #Поиск по ключевым словам в описании транзакции
    if user_input_description == "нет":
        final_list = update_list
    elif user_input_description == "да":
        word_input = input("""Введите ключевое слово для поиска
        """)
        final_list = transactions_search(operation_list=update_list, search_string=word_input)

    #Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    print(f"""Всего банковских операций в выборке: {len(final_list)}""")

    print(final_list)
    # for fi in final_list:
    #     print(fi)
        # unformatted_date = fi["date"]
        # print(unformatted_date)
        # print(type(unformatted_date))

        # formatted_date = get_date(unformatted_date)
        # print(formatted_date)




        # if user_choise == "JSON":
        #     operation_sum = float(fi['operationAmount']['amount'])
        #     operation_currency = fi['operationAmount']['currency']['name']
        #     operation_name = fi["description"]
        # elif user_choise == "CSV" or user_choise == "XLSX":
        #     operation_sum = float(fi['amount'])
        #     operation_currency = fi['currency_name']
        #     operation_name = fi["description"]
        #
        #
        # try:
        #     mask_receiver = mask_account_card(str(fi['to']))
        #     mask_sender = mask_account_card(str(fi['from']))
        # except KeyError:
        #     mask_sender = []
        # if mask_sender == "Данные не введены":
        #     mask_sender = []
        #
        #
        # if mask_sender != []:
        #     print(f"""{formatted_date}  {operation_name},
        #     {mask_sender} -> {mask_receiver},
        #     Сумма: {operation_sum}, {operation_currency}""")
        # else:
        #     print(f"""{formatted_date} {operation_name},
        #     {mask_receiver},
        #     Сумма: {operation_sum} {operation_currency}""")


main()