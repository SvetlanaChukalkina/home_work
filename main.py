from src.utils import get_transactions_info
from src.file_readers import csv_reader, excel_reader

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
        """).lower
        if user_input_sort == "да":
            user_input_range = input("""Отсортировать по возрастанию или по убыванию?
            По возрастанию / по убыванию
            """)
        user_input_currency = input("""Выводить только рублевые тразакции? Да/Нет
        """)

        user_input_description = input("""Отфильтровать список транзакций
        по определенному слову в описании? Да/Нет
        """)

        if user_choise == "JSON":
            initial_data = get_transactions_info(path="data/operations.json")
            # print(initial_data)
        elif user_choise == "CSV":
            initial_data = csv_reader(path="data/transactions.csv")
            print(initial_data)
        # else:
        #     initial_data = (функция чтения XLSX-словаря из папки data)
        #
        # print("Распечатываю итоговый список транзакций...")
#
#     print(f"""Всего банковских операций в выборке:

    # 08.12.2019 Открытие вклада 
    # Счет **4321
    # Сумма: 40542 руб. 
    # 
    # 12.11.2019 Перевод с карты на карту
    # MasterCard 7771 27  3727 -> Visa Platinum 1293 38 **** 9203
    # Сумма: 130 USD
    # 
    # 18.07.2018 Перевод организации 
    # Visa Platinum 7492 65  7202 -> Счет 0034
    # Сумма: 8390 руб.
    # 
    # 03.06.2018 Перевод со счета на счет
    # Счет 2935 -> Счет 4321
    # Сумма: 8200 EUR""")



main()

        # if user_input_status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
        #     print(f'Операции отфильтрованы по статусу {user_input_status.upper()}')
        #     filtered_transaction = []
        #     pattern = re.compile(transaction_search_string=user_input_status, flags=re.IGNORECASE)
        #     for init in initial_data:
        #         if pattern.findall(init["description"]):
        #             filtered_transaction.append(init)

    # if user_input_sort == "да":
    #     функция преобразования даты из модуля, посмотреть, как
    #     подходит к исходным данным


        # if user_input_range.lower() == "по убыванию":
        #     посмотреть по функции