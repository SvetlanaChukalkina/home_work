import csv
import os
import pandas as pd

def csv_reader (path):
    """Cчитывает данные из CSV-файла, возвращает список словарей с транзакциями"""
    try:
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            return list(reader)
    except FileNotFoundError:
        return []


#path = os.path.abspath("../data/transactions.csv")
#print(csv_reader(path))


def excel_reader (path):
    """Cчитывает данные из Excel-файла, возвращает список словарей с транзакциями"""
    try:
        excel_data = pd.read_excel(path)
        excel_data_list = excel_data.to_dict(orient='records')
        return excel_data_list
    except FileNotFoundError:
        return []
#print(excel_reader("../data/transactions_excel.xlsx"))
#print(excel_reader("../data/tranfddfgfdfsactions_excel.xlsx"))
